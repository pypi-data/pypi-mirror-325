import numpy as np
import struct
import math
from pathlib import Path
import yaml
import time 


class lb2_checkRes:
    def __init__(self, download_dir, upload_dir, nStep, mode=0):
        self.download_dir = download_dir
        self.upload_dir = upload_dir
        self.nStep = nStep
        self.nNpu_per_tile = 4
        config_path = Path(download_dir)/"config.json"
        with open(config_path, 'r', encoding='utf8') as stream:
            self.config = yaml.safe_load(stream)
        
        self.nNeuron = self.config['nNeuron']
        self.base = self.config['Base']
        self.dType = self.config['Dtype']
        dType2scale = {0:1,1:2,2:2,3:4}
        self.nNeuron_per_npu = 4096*dType2scale[self.dType] * (self.base+1)
        self.nNeuron_per_tile = self.nNeuron_per_npu * 4
        
        self.mode = mode
        if mode == 0 or mode == 1:
            self.nTile = math.ceil(self.nNeuron/self.nNeuron_per_tile)
            self.nNpu = math.ceil(self.nNeuron/self.nNeuron_per_npu)
        if mode == 2:
            self.nTile = math.ceil(self.nNeuron/(self.nNeuron_per_tile*2))
            self.nNpu = math.ceil(self.nNeuron/(self.nNeuron_per_npu*2))

    def binVSnpy(self, spike_check=True, v_check=True, max_diff=1E-3,save=False):
        nTile = self.nTile
        nStep = self.nStep
        match self.mode:
            case 0 | 1:
                hw_s = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu], dtype=float)
                hw_v = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu], dtype=float)
                hw_wacc1 = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu], dtype=float)
                hw_wacc2 = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu], dtype=float)

            case 2:
                hw_s = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu*2], dtype=float)
                hw_v = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu*2], dtype=float)
                hw_wacc1 = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu*2], dtype=float)
                hw_wacc2 = np.zeros([nStep+1, nTile*self.nNpu_per_tile*self.nNeuron_per_npu*2], dtype=float)

        sw_output_path = self.download_dir + "/soft_data"
        sw_v     = np.load(sw_output_path+"/N_V.npy").astype(np.float32)
        sw_s     = np.load(sw_output_path+"/N_spike.npy").astype(np.int32) 

        for iStep in range(nStep+1):
            for iTile in range(nTile):
                for iNpu in range(self.nNpu_per_tile):
                    offset = iTile * self.nNeuron_per_npu*self.nNpu_per_tile + iNpu * self.nNeuron_per_npu

                    if iStep > 0 and spike_check==True:
                        if self.mode == 0 or self.mode == 1:
                            path = f"{self.upload_dir}/step{iStep}/spike_check/spike_check_tile{iTile}_npu{iNpu}.bin"
                            with open(path, "rb") as f_in:
                                spike_in_npu = np.zeros(self.nNeuron_per_npu)
                                for i in range(self.nNeuron_per_npu):
                                    spike_in_npu[i] = ord(f_in.read(1)) > 0 #129 == \x81, 0 ==\x00
                                spike_in_npu = spike_in_npu.reshape(self.nNeuron_per_npu//8,8)
                                spike_in_npu = spike_in_npu.T.flatten()
                                hw_s[iStep, offset:offset+self.nNeuron_per_npu] = spike_in_npu

                        if self.mode == 2:
                            path_0 = f"{self.upload_dir}/step{iStep}/spike_check/0spike_check_tile{iTile}_npu{iNpu}.bin"
                            with open(path_0, "rb") as f_in:
                                spike_in_npu_0 = np.zeros(self.nNeuron_per_npu)
                                for i in range(self.nNeuron_per_npu):
                                    spike_in_npu_0[i] = ord(f_in.read(1)) > 0 #129 == \x81, 0 ==\x00
                                spike_in_npu_0 = spike_in_npu_0.reshape(self.nNeuron_per_npu//8,8)
                                spike_in_npu_0 = spike_in_npu_0.T.flatten()
                                hw_s[iStep, offset:offset+self.nNeuron_per_npu] = spike_in_npu_0
                            
                            path_1 = f"{self.upload_dir}/step{iStep}/spike_check/1spike_check_tile{iTile}_npu{iNpu}.bin"
                            with open(path_1, "rb") as f_in:
                                spike_in_npu_1 = np.zeros(self.nNeuron_per_npu)
                                for i in range(self.nNeuron_per_npu):
                                    spike_in_npu_1[i] = ord(f_in.read(1)) > 0 #129 == \x81, 0 ==\x00
                                spike_in_npu_1 = spike_in_npu_1.reshape(self.nNeuron_per_npu//8,8)
                                spike_in_npu_1 = spike_in_npu_1.T.flatten()
                                hw_s[iStep, offset+self.nNeuron_per_tile*self.nTile:offset+self.nNeuron_per_npu+self.nNeuron_per_tile*self.nTile] = spike_in_npu_1

                    if v_check==True:
                        if self.mode == 0 or self.mode == 1:
                            path = f"{self.upload_dir}/step{iStep}/weight_check/weight_check_tile{iTile}_npu{iNpu}.bin"
                            with open(path, "rb") as f_in:
                                match (self.base, self.dType):
                                    case (0, 0):
                                        for i in range(self.nNeuron_per_npu):
                                            f_in.read(4*2)
                                            hw_wacc2[iStep, i+offset] = self.bytes2float(f_in.read(4))  
                                            f_in.read(4*1)
                                            hw_wacc1[iStep, i+offset] = self.bytes2float(f_in.read(4))  
                                            hw_v[iStep, i+offset] = self.bytes2float(f_in.read(4)) 
                                            f_in.read(4*2)
                                    case (0, 3):
                                        for i in range(0,self.nNeuron_in_npu, 4):
                                            f_in.read(4*4) 
                                            hw_wacc1[iStep, i+offset+0] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)
                                            hw_wacc1[iStep, i+offset+1] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)
                                            hw_wacc1[iStep, i+offset+2] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)
                                            hw_wacc1[iStep, i+offset+3] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)        

                                            hw_v[iStep, i+offset+0] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)
                                            hw_v[iStep, i+offset+1] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)
                                            hw_v[iStep, i+offset+2] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)
                                            hw_v[iStep, i+offset+3] =  int.from_bytes(f_in.read(1), byteorder='little', signed=True)        
                                            f_in.read(4*2)                                            
                                    case (1, 0):
                                        for i in range(self.nNeuron_per_npu, 2):
                                            f_in.read(4*2)
                                            hw_v[iStep, i+offset] = self.bytes2float(f_in.read(4)) 
                                            f_in.read(4*2)
                                            hw_v[iStep, i+offset] = self.bytes2float(f_in.read(4)) 
                                            f_in.read(4*2)
                        
                        if self.mode == 2:
                            path0 = f"{self.upload_dir}/step{iStep}/weight_check/0weight_check_tile{iTile}_npu{iNpu}.bin"
                            with open(path0, "rb") as f_in:
                                for i in range(self.nNeuron_per_npu):
                                    f_in.read(4*2)
                                    hw_wacc2[iStep, i+offset] = self.bytes2float(f_in.read(4))  
                                    f_in.read(4*1)
                                    hw_wacc1[iStep, i+offset] = self.bytes2float(f_in.read(4))  
                                    hw_v[iStep, i+offset] = self.bytes2float(f_in.read(4)) 
                                    f_in.read(4*2)
                            
                            path1 = f"{self.upload_dir}/step{iStep}/weight_check/1weight_check_tile{iTile}_npu{iNpu}.bin"
                            with open(path1, "rb") as f_in:
                                for i in range(self.nNeuron_per_npu):
                                    f_in.read(4*2)
                                    hw_wacc2[iStep, i+offset+self.nNeuron_per_tile*self.nTile] = self.bytes2float(f_in.read(4))  
                                    f_in.read(4*1)
                                    hw_wacc1[iStep, i+offset+self.nNeuron_per_tile*self.nTile] = self.bytes2float(f_in.read(4))  
                                    hw_v[iStep, i+offset+self.nNeuron_per_tile*self.nTile] = self.bytes2float(f_in.read(4)) 
                                    f_in.read(4*2)

            if spike_check==True:
                s_comp = np.array_equal(hw_s[iStep, :self.nNeuron], sw_s[iStep, :])
                hw_count = int(np.sum(hw_s[iStep,:self.nNeuron]))
                sw_count = int(np.sum(sw_s[iStep]))
                print(f"iStep = {iStep}, s_comp = {s_comp}, hw_count = {hw_count},sw_count = {sw_count}")
                if s_comp == False or hw_count!=sw_count:
                    print("----------------------------------ERROR-----------------------------------------------------")
            
            if v_check==True:
                vDiff = np.abs(hw_v[iStep,:self.nNeuron]-sw_v[iStep])
                print(f"iStep = {iStep}, v_comp_max = {np.max(vDiff)}, ii={np.argmax(vDiff)}")
                if np.max(vDiff) > max_diff:
                    print("----------------------------------ERROR-----------------------------------------------------")
        
        if save == True:
            np.save(self.upload_dir+"/hw_s.npy",hw_s[:,:self.nNeuron])
            np.save(self.upload_dir+"/hw_v.npy",hw_v[:,:self.nNeuron])
            np.save(self.upload_dir+"/hw_wacc1.npy",hw_wacc1[:,:self.nNeuron])
            np.save(self.upload_dir+"/hw_wacc2.npy",hw_wacc2[:,:self.nNeuron])
            print(f"npy files saved in {self.upload_dir}")

    def npyVSnpy(self,scale_factor1=0.8,scale_factor2=0.9,max_diff=1E-3):
        nNpu =self.nTile*self.nNpu_per_tile
        sw_output_path = self.download_dir + "/soft_data"

        hw_s     = np.load(self.upload_dir+"/hw_s.npy").astype(np.int32) 
        hw_v     = np.load(self.upload_dir+"/hw_v.npy").astype(np.float32)
        hw_wacc1 = np.load(self.upload_dir+"/hw_wacc1.npy").astype(np.float32)
        hw_wacc1 *= (1/scale_factor1) #scale_factor = 1-dt/tau for syn
        hw_wacc2 = np.load(self.upload_dir+"/hw_wacc2.npy").astype(np.float32)
        hw_wacc2 *= (1/scale_factor2) #scale_factor = 1-dt/tau for syn
        sw_s     = np.load(sw_output_path+"/N_spike.npy").astype(np.int32) 
        sw_v     = np.load(sw_output_path+"/N_V.npy").astype(np.float32)
        sw_wacc1 = np.load(sw_output_path+"/N_wacc1.npy").astype(np.float32)
        sw_wacc2 = np.load(sw_output_path+"/N_wacc2.npy").astype(np.float32)

        for iStep in range(self.nStep+1):
            hw_count = int(np.sum(hw_s[iStep]))
            iNeuron_spike_hw = np.nonzero(hw_s[iStep])[0]
            sw_count = np.sum(sw_s[iStep])
            iNeuron_spike_sw = np.nonzero(sw_s[iStep])[0]
            s_comp = np.array_equal(iNeuron_spike_hw, iNeuron_spike_sw)

            vDiff = np.abs(hw_v[iStep]-sw_v[iStep])
            waccDiff = np.abs(hw_wacc1[iStep]-sw_wacc1[iStep]) + np.abs(hw_wacc2[iStep]-sw_wacc2[iStep])

            print(f"iStep = {iStep}, s_comp = {s_comp}, hw_count = {hw_count},sw_count = {sw_count}")
            print(f"iStep = {iStep}, v_comp_max = {np.max(vDiff)}, ii={np.argmax(vDiff)}")
            print(f"iStep = {iStep}, wacc_comp_max = {np.max(waccDiff)}, ii={np.argmax(waccDiff)}")
            
            if np.max(vDiff) > max_diff or np.max(waccDiff) > max_diff or s_comp==False or hw_count!=sw_count or np.isnan(np.max(vDiff)):
                print("----------------------------------ERROR-----------------------------------------------------")
                iNeoron_vDiff = np.nonzero(vDiff> max_diff)[0]
                iNeoron_waccDiff = np.nonzero(waccDiff> max_diff)[0]
                iNeoron_spike_hw_unique,iNeoron_spike_sw_unique =  self.removeCommon(iNeuron_spike_hw, iNeuron_spike_sw)
                iNeoron_wacc_hw_unique,iNeoron_wacc_sw_unique =  self.removeCommon(iNeuron_spike_hw, iNeuron_spike_sw)

                npu_check = []
                for iNpu in range(self.nNpu*2):
                    istart = int(iNpu*(self.nNeuron_per_npu))
                    iend = int((iNpu+1)*(self.nNeuron_per_npu))
                    sw_v_local = sw_v[iStep,istart:iend] 
                    hw_v_local = hw_v[iStep,istart:iend]
                    vDiff_local = np.abs(hw_v_local-sw_v_local)
                    if np.max(vDiff_local)<=max_diff:
                        npu_check.append(1)
                    else:
                        npu_check.append(0)
                print(f"iStep = {iStep}, npu_check = {npu_check}")

    def bytes2float(self,v) -> float:
        return struct.unpack('f', struct.pack('4B', *[v[0], v[1], v[2], v[3]]))[0]

    def returnMaxMin(self,x):
        return np.max(x), np.min(x)

    def removeCommon(self,list_a,list_b):
        common_elements = set(list_a) & set(list_b)
        list_a = [item for item in list_a if item not in common_elements]
        list_b = [item for item in list_b if item not in common_elements]
        return list_a, list_b

    def receive_spike(self,data):
        return [i for i in range(1, len(data)) if data[i] > data[i - 1]]
