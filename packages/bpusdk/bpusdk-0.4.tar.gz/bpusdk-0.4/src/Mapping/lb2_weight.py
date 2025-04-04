#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Yukun Feng
# @Date: 2024-05-29

"""Network adapter base class
"""
import os
import shutil
import warnings
from functools import cached_property, partial, reduce
from pathlib import Path
import numpy as np
from loguru import logger
from BrainpyLib.Common import get_hex_data, reverse_by_group
from Mapping.W2H import Transform_Weight_Index
import math
warnings.filterwarnings("ignore")

class lb2_Weight():
    def __init__(self, connection_matrix, neuron_num, neuron_scale, V_init, config,mode=0) -> None:
        self.connection_matrix = connection_matrix  
        self.neuron_num = neuron_num
        self.V_init = V_init
        self.config = config
        self.mode = mode

        Ex_num = neuron_scale[0]
        Ih_num = neuron_scale[1]

        self.fanout = 10
        self.weight_addr_0 = 0
        self.nNeuron_per_Npu = config['Npu_NeuronNum']
        self.nNeuron_per_tile = config['Npu_NeuronNum'] * config['Tile_NpuNum']
        self.nRow = config['nRow']       
        self.nCol = config['nCol']
        self.nTile = config['nTile']
        self.base = config['Base']
        self.nTile_layout = self.nRow*self.nCol
        self.nNpu_layout = self.nTile_layout*4

        self.generator = Transform_Weight_Index(Ex_num, Ih_num, config)
        self._dtype = config['Dtype']
        self.V_init = np.array(V_init)

        if self._dtype == 'int8':
            self.V_init = np.floor(self.V_init)
            self.V_init = reverse_by_group(self.V_init,4)

        if config["Base"] == 2:
            self.V_init_0 = self.V_init[::2]  # even indices starting by 0
            self.V_init_1 = self.V_init[1::2]  # even indices starting by 1

    @cached_property
    def get_init_value(self):
        match (self.config['Base'], self._dtype):
            case (1, 'fp32'):
                init_value = int(np.single(-60.).view("uint32").astype("<u4")) #needed
                npu_content = [[] for _ in range(self.nNpu_layout)]
                for iNpu in range(self.nNpu_layout):
                    iStart = iNpu * self.nNeuron_per_Npu
                    npu_content_local = np.array([
                        [1] * self.nNeuron_per_Npu, [1] * self.nNeuron_per_Npu, [0] * self.nNeuron_per_Npu, [0] * self.nNeuron_per_Npu, [10] * self.nNeuron_per_Npu,
                        [init_value] * self.nNeuron_per_Npu, 
                        [0] * self.nNeuron_per_Npu, [0] * self.nNeuron_per_Npu, [0] * self.nNeuron_per_Npu, [0] * self.nNeuron_per_Npu, [0] * self.nNeuron_per_Npu,
                    ])
                    V_init_in_npu = self.V_init[iStart:iStart+self.nNeuron_per_Npu]
                    npu_content_local[5,:len(V_init_in_npu)] = np.array(V_init_in_npu).view("uint32").astype("<u4")
                    npu_content[iNpu] = npu_content_local

            case (1, 'fp16'):
                nNeuron_in_npu = 4096
                init_value = int(np.float16(10).view("uint16"))
                npu_content = [[] + [] for i in range(self.nNpu_layout)]
                for iNpu in range(self.nNpu_layout):
                    npu_content[iNpu] = [
                        [1] * nNeuron_in_npu, [1] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [10] * nNeuron_in_npu,
                        [init_value] * nNeuron_in_npu,         # 3,0
                        [init_value] * nNeuron_in_npu,         # 2,0
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                    ]
            case (1, 'int8'):
                init_value = int(np.int8(2.).view("uint8"))
                nNeuron_in_npu = 4096
                npu_content = [[] for _ in range(self.nNpu_layout)]
                for iNpu in range(self.nNpu_layout):
                    npu_content_local = [
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [33] * nNeuron_in_npu,         # 3,0
                        [22] * nNeuron_in_npu,         # 2,0
                        [11] * nNeuron_in_npu,         # 1,0
                        [00] * nNeuron_in_npu,         # 0,0
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                    ]
                    iStart = iNpu * nNeuron_in_npu
                    npu_content_local = np.array(npu_content_local)
                    V_init_in_npu = self.V_init[:,iStart:iStart+nNeuron_in_npu]
                    npu_content_local[5:9,:V_init_in_npu.shape[1]] = np.array(V_init_in_npu).astype("int8").copy().view("uint8")
                    npu_content[iNpu] = npu_content_local
            case (2, 'fp16'):
                nNeuron_in_npu = 4096
                init_value = int(np.float16(10).view("uint16"))
                npu_content = [[] for _ in range(self.nNpu_layout)]
                for iNpu in range(self.nNpu_layout):
                    npu_content[iNpu] = [
                        [1] * nNeuron_in_npu, [1] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [10] * nNeuron_in_npu,

                        [init_value] * nNeuron_in_npu,         # 3,0
                        [init_value] * nNeuron_in_npu,         # 2,0
                        [0] * nNeuron_in_npu,                  # 3,1
                        [0] * nNeuron_in_npu,                  # 2,1
                        [0] * nNeuron_in_npu,                  # 3,2
                        [0] * nNeuron_in_npu,                  # 2,2

                        [init_value] * nNeuron_in_npu,
                        [init_value] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu,
                    ]
            case (2, 'fp32'):
                nNeuron_in_npu = 4096
                init_value = int(np.single(-60.0).view("uint32").astype("<u4"))
                npu_content = [[] for _ in range(self.nNpu_layout)]
                for iNpu in range(self.nNpu_layout):
                    iStart = iNpu * nNeuron_in_npu
                    npu_content_local = [
                        [1] * nNeuron_in_npu, [1] * nNeuron_in_npu,[0] * nNeuron_in_npu,[0] * nNeuron_in_npu,[10] * nNeuron_in_npu,

                        [init_value] * nNeuron_in_npu,         # 1,0
                        [0] * nNeuron_in_npu,                  # 1,1
                        [0] * nNeuron_in_npu,                  # 1,2

                        [init_value] * nNeuron_in_npu,         # 0,0
                        [0] * nNeuron_in_npu,                  # 0,1
                        [0] * nNeuron_in_npu,                  # 0,2
                    ]

                    npu_content_local = np.array(npu_content_local)
                    V_init_1_in_npu = self.V_init_1[iStart:iStart+nNeuron_in_npu]
                    V_init_0_in_npu = self.V_init_0[iStart:iStart+nNeuron_in_npu]
                    
                    npu_content_local[5,:len(V_init_1_in_npu)] = np.array(V_init_1_in_npu).view("uint32").astype("<u4")
                    npu_content_local[8,:len(V_init_0_in_npu)] = np.array(V_init_0_in_npu).view("uint32").astype("<u4")
                    npu_content[iNpu] = npu_content_local

            case (2, 'int8'):
                nNeuron_in_npu = 4096
                init_value = int(np.int8(6.).view("uint8"))
                npu_content = [[] + [] for i in range(self.nNpu_layout)]
                for iNpu in range(self.nNpu_layout):
                    npu_content[iNpu] = [
                        [1] * nNeuron_in_npu,
                        [1] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu,

                        [10] * nNeuron_in_npu,

                        [init_value] * nNeuron_in_npu,         # 7,0
                        [init_value] * nNeuron_in_npu,         # 6,0
                        [init_value] * nNeuron_in_npu,         # 5,0
                        [init_value] * nNeuron_in_npu,         # 4,0
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [init_value] * nNeuron_in_npu,         # 3,0
                        [init_value] * nNeuron_in_npu,         # 2,0
                        [init_value] * nNeuron_in_npu,         # 1,0
                        [init_value] * nNeuron_in_npu,         # 0,0
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                        [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu, [0] * nNeuron_in_npu,
                    ]
        return npu_content
    
    #The receiving direction for dst_id
    def determineRouting(self,scr_id,dst_id,X_TileNum, Y_TileNum):
        population_size = 1024
        scr_iPopulation = scr_id//(population_size)
        dst_iPopulation = dst_id//(population_size)
        scr_iTile = scr_iPopulation//16
        dst_iTile = dst_iPopulation//16

        if scr_iTile == dst_iTile:
            return 0 #local
        
        elif dst_iTile - scr_iTile == -X_TileNum:
            return 2 #down
        
        elif dst_iTile - scr_iTile == X_TileNum:
            return 1 #up

        elif scr_iTile % X_TileNum != 0 and dst_iTile-scr_iTile == -1:
            return 4 #right

        elif dst_iTile % X_TileNum != 0 and dst_iTile-scr_iTile == 1:
            return 3 #left

        else:
            raise NotImplementedError # tiles multiple step apart
    
    def createDst_weight(self,connection_matrix ,X_TileNum, Y_TileNum):
        tot_TileNum = X_TileNum*Y_TileNum
        conn_matrix_inter = [ [] + [{},{},{},{},{}] for _ in range(tot_TileNum*4)]

        #sort connection_matrix to conn_matrix_inter based by direction
        FP32 = lambda x: np.single(x).view("uint32").astype("<u4")
        for src_id in connection_matrix:
            dst_list =  connection_matrix[src_id]
            for dst_id in dst_list:
                direction = self.determineRouting(src_id,dst_id,X_TileNum, Y_TileNum)
                dst_iNpu = dst_id//4096
                if src_id not in conn_matrix_inter[dst_iNpu][direction]:
                    conn_matrix_inter[dst_iNpu][direction][src_id] = {}
                conn_matrix_inter[dst_iNpu][direction][src_id][dst_id] = connection_matrix[src_id][dst_id]

        #write conn_matrix_inter as index and weight per npu
        relevant_directions = [0,3,1]
        index_data = [np.zeros(4096*4*len(relevant_directions)) for _ in range(tot_TileNum*4)] 
        weight_data = [ [] + [] for _ in range(tot_TileNum*4)]    
        for idirection,direction in enumerate(relevant_directions):
            for iNpu in range(tot_TileNum*4):
                for src_id in conn_matrix_inter[iNpu][direction]:
                    dst_list = conn_matrix_inter[iNpu][direction][src_id]
                    for dst_id in dst_list:
                        weight = FP32(conn_matrix_inter[iNpu][direction][src_id][dst_id])
                        if src_id < 576*1024/2 :
                            dst_and_weight = []
                            dst_and_weight += [dst_id % 16384, 0, weight, 0, 0, 0, 0, 0]
                        else:
                            dst_and_weight = []
                            dst_and_weight += [dst_id % 16384, 0, 0, weight, 0, 0, 0, 0]
                        index_data[iNpu][src_id % 16384 + idirection*16384] += 1
                        weight_data[iNpu].append(dst_and_weight)
        dst_weight = [weight_data,None,index_data]
        return dst_weight
    
    def genLog(self,dst_weight,mode):
        weight_write_list = dst_weight[0]
        nConn_in_npu = [len(weight_write_list[i]) for i in range(len(weight_write_list))]

        weight_per_conn = 256
        space_needed_in_npu = np.array(nConn_in_npu) * weight_per_conn
        
        KB = 1024 * 8
        index_space = 128 * KB
        weight_space = 1280 * KB
        dTypedict = {'int8':4,'int16':2,'fp16':2,'fp32':1}
        nNeuron_per_group = dTypedict[self._dtype]*self.base
        index_per_neuron = 32/nNeuron_per_group
        index = index_per_neuron*self.nTile_layout*self.nNeuron_per_tile
        index_in_weight = max(0,index - index_space)
        weight_avalible = weight_space - index_in_weight


        nConn_in_tile = np.array([sum(nConn_in_npu[i:i + 4]) for i in range(0, len(nConn_in_npu), 4)])
        self.syn_calcu_tw = math.ceil(np.max(nConn_in_tile)/4*30*10)

        self.log = ["-----------Weight-----------\n"]
        nConn = np.sum(nConn_in_tile)
        fanout = nConn/self.neuron_num
        self.log.append(f"nConn total: {nConn}, corresponding fanout: {fanout:.2f}\n")
        nConn_in_tile = np.array(nConn_in_tile).reshape(self.nRow, self.nCol)
        self.log.append("nConn in each tile: \n")
        for i in nConn_in_tile:
            data = str(i) + '\n'
            self.log.append(data)
        self.log[-1] += '\n'

        if mode == 0:
            check = space_needed_in_npu > weight_avalible
            if len(np.nonzero(check)[0]) > 0:
                logger.warning(f'nConn in following npu exceeds limit: {np.nonzero(check)[0]}')
                with open("./log.txt", "w") as file:
                    file.write(" ".join(self.log))
                exit()


    def write_to_bin(self, output_dir):
        output_dir = Path(output_dir)
        output_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
        mode = self.mode

        index_path_list = []
        weight_path_list_split = []
        ncu_path_list = []
        index_dir = output_dir / 'index'
        weight_dir = output_dir / 'weight'
        ncu_dir = output_dir / 'ncu'

        if not index_dir.exists():
            os.makedirs(index_dir)
        if not weight_dir.exists():
            os.makedirs(weight_dir)
        if not ncu_dir.exists():
            os.makedirs(ncu_dir)

        for i in range(self.generator.npu_num):
            index_path_list.append(
                index_dir / f'index_tile{i // 4}_npu{i % 4}.bin')
            weight_path_list_split.append(
                weight_dir / f'weight_tile{i // 4}_npu{i % 4}.bin')
            ncu_path_list.append(
                ncu_dir / f'ncu_tile{i // 4}_npu{i % 4}.bin')

        spike_dir = output_dir / 'spike'
        os.makedirs(spike_dir, exist_ok=True)
        file_size = 32*1024
        file_name = "spike.bin"
        outfile_path = spike_dir /file_name
        with open(outfile_path, "wb") as f:
            f.write(bytearray([0x00] * file_size))

        dst_weight = self.generator(connection_matrix=self.connection_matrix)

        if mode == 1:
            dst_weight = self.createDst_weight(connection_matrix=self.connection_matrix,X_TileNum=6,Y_TileNum=6)
        self.genLog(dst_weight,mode=mode)

        self.gen_bin_file(npu_num=self.generator.npu_num,
                          weight_path_list_split=weight_path_list_split,
                          index_path_list=index_path_list,
                          weight_write_list=dst_weight[0],
                          index_suffix=dst_weight[2],
                          ncu_path_list=ncu_path_list,
                          mode = mode)
                              
    def write_to_hex(self, output_dir):
        output_dir = Path(output_dir)
        output_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
        dst_weight = self.generator(connection_matrix=self.connection_matrix)

        index_path_list = []
        weight_path_list = []
        ncu_path_list = []

        index_dir = output_dir / 'hex' / 'index'
        weight_dir = output_dir / 'hex' / 'weight'
        ncu_dir = output_dir / 'hex' / 'ncu'

        if index_dir.exists():
            shutil.rmtree(index_dir)
        os.makedirs(index_dir)

        if weight_dir.exists():
            shutil.rmtree(weight_dir)
        os.makedirs(weight_dir)

        if ncu_dir.exists():
            shutil.rmtree(ncu_dir)
        os.makedirs(ncu_dir)

        for i in range(self.generator.npu_num):
            index_path_list.append(
                index_dir / f'index_tile{i//4}_npu{i%4}.hex')
            weight_path_list.append(
                weight_dir / f'weight_tile{i//4}_npu{i%4}.hex')
            ncu_path_list.append(
                ncu_dir/ f'ncu_tile{i//4}_npu{i%4}.hex')
        
        self.gen_hex_file(npu_num=self.generator.npu_num, index_suffix=dst_weight[2], weight_write_list=dst_weight[0],
                     weight_path_list=weight_path_list, index_path_list=index_path_list, ncu_path_list=ncu_path_list)

    def gen_hex_file(self, npu_num, index_suffix, weight_write_list,
                     weight_path_list, index_path_list, ncu_path_list):
        mode = self.mode

        #NCU
        lens = self.generator.ncu_state[self._dtype]['lens']
        prefix = self.generator.ncu_state[self._dtype]['prefix'][self.generator.base]

        for iNpu in range(self.generator.npu_num):
            temp = np.array(self.get_init_value[iNpu]).T
            for iNpu in range(0, temp.shape[0]):
                data_tmp = list(map(lambda x: get_hex_data(
                    hex(x), lens=lens), temp[iNpu][5:]))
                data_tmp = reduce(lambda x, y: x + y, data_tmp)
                with open(ncu_path_list[iNpu], 'a') as f_in:
                    f_in.write(prefix + data_tmp + '\n')

        #Index and Weight
        if mode == 0 or mode == 1:
            index_suffix = np.array(index_suffix)
            resultses = []
            fanout = 12

            for iNpu in range(npu_num):
                dst_id_count = []
                dst_id_count += np.int32(index_suffix[iNpu]).tolist()
                dst_id_cumsum = np.cumsum([self.weight_addr_0] + dst_id_count[:-1])  # 权重矩阵的地址要动态变化
                resultses.append((dst_id_cumsum << fanout).astype("<u4") + np.array(dst_id_count).astype("<u4"))
            for ids in range(npu_num):
                index_path = index_path_list[ids]
                weight_path = weight_path_list[ids]
                temp = resultses[ids]
                temp = temp.reshape(-1, 8)  # (, 8)
                count = 0
                for item in range(temp.shape[0]):
                    count += 1
                    var = list(map(lambda x: get_hex_data(hex(x)), temp[item][:]))
                    var = reduce(lambda x, y: x + y, reversed(var))
                    new_var = var

                    # if count <= 4096:
                    #     with open(index_path, 'a') as f_in:
                    #         f_in.write(new_var + '\n')
                    # else:
                    #     with open(weight_path, 'a') as f_in:
                    #         f_in.write(new_var + '\n')
                    with open(index_path, 'a') as f_in:
                        f_in.write(new_var + '\n')

                temp = weight_write_list[ids]
                for iNpu in range(len(temp)):
                    var = list(map(lambda x: get_hex_data(hex(x)), temp[iNpu]))
                    var = reduce(lambda x, y: x + y, var)
                    new_var = var
                    with open(weight_path, 'a') as f_in:
                        f_in.write(new_var + '\n')

                iRow = 40960 - (count-4096)-len(temp)
                padding_zeros_0  = '0000000000000000000000000000000000000000000000000000000000000000\n' * iRow
                
                with open(weight_path, 'a') as f_in:
                    f_in.write(padding_zeros_0)
        
        if mode == 2:
            index_suffix = np.array(index_suffix)
            weight_write_list = np.array(weight_write_list)


            resultses = []
            fanout = 12
            
            resultses = []
            fanout = 12
            dst_id_count_list = []
            dst_id_cumsum_list = []
            resultses = []
            fanout = 12
            for iNpu in range(npu_num):
                iTile = iNpu //4
                split = int(self.nTile/2)
                dst_id_count = []
                if iTile>=split:
                    dst_id_count += np.int32(index_suffix[iNpu]).tolist()
                    dst_id_cumsum = np.cumsum([self.weight_addr_0] + dst_id_count[:-1])
                    mask = np.array(dst_id_count) > 0
                    dst_id_cumsum[mask] += dst_id_cumsum_list[iNpu-split*4][-1] + dst_id_count_list[iNpu-split*4][-1]
                    dst_id_count_list.append(dst_id_count)
                    dst_id_cumsum_list.append(dst_id_cumsum)
                else:
                    dst_id_count += np.int32(index_suffix[iNpu]).tolist()
                    dst_id_cumsum = np.cumsum([self.weight_addr_0] + dst_id_count[:-1])  
                    dst_id_count_list.append(dst_id_count)
                    dst_id_cumsum_list.append(dst_id_cumsum)
                resultses.append((dst_id_cumsum << fanout).astype("<u4") + np.array(dst_id_count).astype("<u4"))
            
            for ids in range(npu_num):
                index_path = index_path_list[ids]
                weight_path = weight_path_list[ids]
                temp = resultses[ids]
                temp = temp.reshape(-1, 8)  # (, 8)
                count = 0
                for item in range(temp.shape[0]):
                    count += 1
                    var = list(map(lambda x: get_hex_data(hex(x)), temp[item][:]))
                    var = reduce(lambda x, y: x + y, reversed(var))
                    new_var = var

                    # if count <= 4096:
                    #     with open(index_path, 'a') as f_in:
                    #         f_in.write(new_var + '\n')
                    # else:
                    #     with open(weight_path, 'a') as f_in:
                    #         f_in.write(new_var + '\n')
                    with open(index_path, 'a') as f_in:
                        f_in.write(new_var + '\n')

                temp = weight_write_list[ids]
                for iNpu in range(len(temp)):
                    var = list(map(lambda x: get_hex_data(hex(x)), temp[iNpu]))
                    var = reduce(lambda x, y: x + y, var)
                    new_var = var
                    with open(weight_path, 'a') as f_in:
                        f_in.write(new_var + '\n')

    @staticmethod
    def trans_line(x):
        result = []
        for item in range(len(x), 0, -8):
            tmp = []
            var = x[item-8:item]
            tmp.extend([var[6:8], var[4:6], var[2:4], var[0:2]])
            tmp = list(map(lambda x: int(x, 16), tmp))
            result.extend(tmp)
        return result

    def gen_bin_file(self, npu_num, index_suffix, weight_write_list,
                     weight_path_list_split, index_path_list, ncu_path_list,mode):
        #NCU
        prefix = self.generator.ncu_state[self._dtype]['prefix'][self.generator.base]
        for iNpu in range(self.generator.npu_num):
            ncu_path = ncu_path_list[iNpu]
            temp = (np.array(self.get_init_value[iNpu]).T)[:, 5:]
            ncu_content = []
            for i in range(temp.shape[0]):
                var = list(map(lambda x: get_hex_data(hex(x),lens=self.generator.ncu_state[self._dtype]['lens']), temp[i][:]))
                var = prefix + reduce(lambda x, y: x + y, var)
                new_var = self.trans_line(var)
                ncu_content.extend(new_var)
            with open(ncu_path, 'wb') as f_in:
                f_in.write(bytearray(ncu_content))
        
        #index + weight
        if mode == 0 or mode == 1:
            index_suffix = np.array(index_suffix)
            resultses = []
            fanout = 12

            for i in range(npu_num):
                dst_id_count = []
                dst_id_count += np.int32(index_suffix[i]).tolist()
                dst_id_cumsum = np.cumsum([self.weight_addr_0] + dst_id_count[:-1])  # 权重矩阵的地址要动态变化
                resultses.append((dst_id_cumsum << fanout).astype("<u4") + np.array(dst_id_count).astype("<u4"))
            for iNpu in range(npu_num):
                index_path = index_path_list[iNpu]
                temp = resultses[iNpu]
                temp = temp.reshape(-1, 8)  # (, 8)
                self.index_data = [] #in byte
                for iRow in range(temp.shape[0]):
                    var = list(map(lambda x: get_hex_data(hex(x)), temp[iRow][:]))
                    var = reduce(lambda x, y: x + y, reversed(var))
                    new_var = self.trans_line(var)
                    self.index_data.extend(new_var)
                
                index_in_index = bytearray(self.index_data[:4096*32])
                if len(self.index_data) <= 4096*32:
                    padding_zeros_0 = [int('00', 16)] * (4096 - int(len(index_in_index) / 32)) * 32
                    with open(index_path, 'wb') as f_in:
                        f_in.write(index_in_index)
                        f_in.write(bytearray(padding_zeros_0))
                else:
                    with open(index_path, 'wb') as f_in:
                        f_in.write(index_in_index)
                    index_in_weight = bytearray(self.index_data[4096*32:])

                with open(weight_path_list_split[iNpu], 'wb') as f_in:
                    if len(self.index_data) > 4096*32:
                        f_in.write(index_in_weight)
                    weight_write_list_per_npu = weight_write_list[iNpu]
                    content = []
                    for i in range(len(weight_write_list_per_npu)):
                        var = list(map(lambda x: get_hex_data(hex(x)), weight_write_list_per_npu[i]))
                        var = reduce(lambda x, y: x + y, var)
                        new_var = self.trans_line(var)
                        content.extend(new_var)
                    f_in.write(bytearray(content))

                    index_in_weight = max(0,(len(self.index_data) - 128*1024))
                    weight_padding =  max(0,math.ceil((1280*1024-index_in_weight-len(content))))
                    f_in.write(bytearray([0x00] * weight_padding))
                
        #index + weight
        if mode == 2:
            index_suffix = np.array(index_suffix)
            weight_write_list = np.array(weight_write_list)
            
            dst_id_count_list = []
            dst_id_cumsum_list = []
            resultses = []
            fanout = 12
            for i in range(npu_num):
                iTile = i //4
                split = int(self.nTile/2)
                dst_id_count = []
                if iTile>=split:
                    dst_id_count += np.int32(index_suffix[i]).tolist()
                    dst_id_cumsum = np.cumsum([self.weight_addr_0] + dst_id_count[:-1])
                    mask = np.array(dst_id_count) > 0
                    dst_id_cumsum[mask] += dst_id_cumsum_list[i-split*4][-1] + dst_id_count_list[i-split*4][-1]
                    dst_id_count_list.append(dst_id_count)
                    dst_id_cumsum_list.append(dst_id_cumsum)
                else:
                    dst_id_count += np.int32(index_suffix[i]).tolist()
                    dst_id_cumsum = np.cumsum([self.weight_addr_0] + dst_id_count[:-1])  
                    dst_id_count_list.append(dst_id_count)
                    dst_id_cumsum_list.append(dst_id_cumsum)
                resultses.append((dst_id_cumsum << fanout).astype("<u4") + np.array(dst_id_count).astype("<u4"))
            
            for iNpu in range(npu_num):
                index_path = index_path_list[iNpu]
                temp = resultses[iNpu]
                temp = temp.reshape(-1, 8)  # (, 8)
                self.index_data = [] #in byte
                for iRow in range(temp.shape[0]):
                    var = list(map(lambda x: get_hex_data(hex(x)), temp[iRow][:]))
                    var = reduce(lambda x, y: x + y, reversed(var))
                    new_var = self.trans_line(var)
                    self.index_data.extend(new_var)
                
                with open(index_path, 'wb') as f_in:
                    f_in.write(bytearray(self.index_data))

                with open(weight_path_list_split[iNpu], 'wb') as f_in:
                    weight_write_list_per_npu = weight_write_list[iNpu]
                    content = []
                    for i in range(len(weight_write_list_per_npu)):
                        var = list(map(lambda x: get_hex_data(hex(x)), weight_write_list_per_npu[i]))
                        var = reduce(lambda x, y: x + y, var)
                        new_var = self.trans_line(var)
                        content.extend(new_var)
                    f_in.write(bytearray(content))

    def merge_weight(self,download_dir):
        index_size = os.path.getsize(f"{download_dir}/index/index_tile{0}_npu{0}.bin")
        spike_size = 32*1024 # Byte
        ncu_size = 128*1024

        split = int(self.nTile/2)
        for iTile in range(split):
            for iNpu in range(4):
                with open(f"{download_dir}/index/index_tile{iTile}_npu{iNpu}.bin", 'rb') as source_file:
                    index0 = source_file.read()  
                    
                with open(f"{download_dir}/index/index_tile{iTile+split}_npu{iNpu}.bin", 'rb') as source_file:
                    index1 = source_file.read()  

                with open(f"{download_dir}/weight/weight_tile{iTile}_npu{iNpu}.bin", 'rb') as source_file:
                    weight0 = source_file.read()  
                    weight0_size = os.path.getsize(f"{download_dir}/weight/weight_tile{iTile}_npu{iNpu}.bin")

                with open(f"{download_dir}/weight/weight_tile{iTile+split}_npu{iNpu}.bin", 'rb') as source_file:
                    weight1 = source_file.read()  
                    weight1_size = os.path.getsize(f"{download_dir}/weight/weight_tile{iTile+split}_npu{iNpu}.bin")

                with open(f"{download_dir}/ncu/ncu_tile{iTile}_npu{iNpu}.bin", 'rb') as source_file:
                    ncu0 = source_file.read()  

                with open(f"{download_dir}/ncu/ncu_tile{iTile+split}_npu{iNpu}.bin", 'rb') as source_file:
                    ncu1 = source_file.read()  

                data = []
                weight_padding_size = (128+1280)*1024 -index_size*3-weight0_size-weight1_size-ncu_size*2-spike_size*3
                if weight_padding_size<0:
                    print("weight exceed limit")
                    exit()
                data.extend(bytearray([0x00] *index_size))   #128
                data.extend(bytearray(weight0))              #128
                data.extend(bytearray(weight1))              #128
                data.extend(bytearray([0x00] *weight_padding_size))     #416
                data.extend(bytearray(index0))               #128
                data.extend(bytearray(index1))               #128
                data.extend(bytearray(ncu0))                 #128
                data.extend(bytearray(ncu1))                 #128
                data.extend(bytearray([0x00] *spike_size))   #32
                data.extend(bytearray([0x00] *spike_size))   #32
                data.extend(bytearray([0x00] *spike_size))   #32

                os.remove(f"{download_dir}/index/index_tile{iTile}_npu{iNpu}.bin")
                os.remove(f"{download_dir}/weight/weight_tile{iTile}_npu{iNpu}.bin")

                with open(f"{download_dir}/index/index_tile{iTile}_npu{iNpu}.bin", 'wb') as destination_file:
                    destination_file.write(bytearray(data[:128*1024]))

                with open(f"{download_dir}/weight/weight_tile{iTile}_npu{iNpu}.bin", 'wb') as destination_file:
                    destination_file.write(bytearray(data[128*1024:]))
