# 对不同dtype、base和split的数据处理转换成hex数据
import numpy as np
from functools import reduce
from BrainpyLib.Common import get_hex_data, quantize
from operator import methodcaller
import math
class Transform_Weight_Index:
    def __init__(self, ex_num, ih_num,config) -> None:
        self.base = config['Base']
        self.split = config['Split']
        self.ex_num = ex_num
        self.ih_num = ih_num
        self._dtype = config['Dtype']
        self.tile_num = config['nRow']  * config['nCol']
        self.npu_num = self.tile_num*4

        # 外加np.int32防止写入weight_value时 weight_value << 24 出现高位截断导致写入的权重值为0
        FP32 = lambda x: np.single(x).view("uint32").astype("<u4")
        FP16 = lambda x: np.int32(np.float16(x).view("uint16"))
        INT8 = lambda x: np.int32(np.int8(quantize(x,0, _type = 8)).view("uint8"))

        assert self.base in [1, 2] and self.split in [1, 2, 4], "base should be [1, 2] and split should be in [1, 2, 4]."
        self.ncu_state = {"fp32" : {'lens' : 8, 'prefix' : { 1 : '80000000a0000000', 2 : 'C0000000aa000000'}, "scale" : 4096, "row" : 1},
                        "fp16" : {'lens' : 4, 'prefix' : { 1 : 'C0000000aa000000', 2 : 'F0000000aaaa0000'}, "scale" : 8192, "row" : 2},
                        "int8"    : {'lens' : 2, 'prefix' : { 1 : 'F0000000aaaa0000', 2 : 'FF000000aaaaaaaa'}, "scale" : 16384, "row" : 4}}    
        self.trans_type = {'fp32' : FP32, 'fp16' : FP16, 'int8' : INT8, 'int16' : FP16}    
        self.nNeuron_per_Npu = self.ncu_state[self._dtype]['scale'] * self.base
        self.nNeuron_per_tile = config['Tile_NpuNum'] * self.nNeuron_per_Npu
        self.total_num = ex_num + ih_num
        self.total_num = math.ceil(self.total_num/self.nNeuron_per_tile)*self.nNeuron_per_tile #to make the addr calcu coorect

        self.weight_source_list = [ [] + [] for _ in range(self.npu_num)]
        self.weight_write_list = [ [] + [] for _ in range(self.npu_num)]
        self.index_suffix = [ [] + [] for _ in range(self.npu_num)]
        
    def __call__(self, connection_matrix):
        """Call different sub functions according to the split and base. 
        """
        self.connection_matrix = connection_matrix
        kernel = f"transform_sp{self.split}_b{self.base}"
        print("Running kernel: ", kernel)
        print(f"dtype: {self._dtype}")
        methodcaller(kernel)(self)
        return self.weight_write_list, self.weight_source_list, self.index_suffix
    
    def mix_dict(self, num_per_row, dict_list):
        """for each row make sure all elements have identical keys.
        If not connected, write weight as 0. 
        """        
        if num_per_row == 1:
            return dict_list
        for part in range(self.npu_num):
            tmp_part = dict_list[part]
            for ids in range(num_per_row):
                tmp_ids = tmp_part[ids]
                tmp_others = tmp_part[:ids] + tmp_part[ids + 1:]
                new_key = []
                for element in tmp_others:
                    new_key += list(element.keys() - tmp_ids.keys())
                zeros = [0] * len(new_key)
                pad_dict = dict(zip(new_key, zeros))
                tmp_ids.update(pad_dict)
        return dict_list
        
    def transform_sp1_b1(self):
        self.num_per_sram_row = self.ncu_state[self._dtype]["row"] * self.base
        for src_id in range(int(self.total_num // self.num_per_sram_row)):
            tmp_dict_list = [[{} for i in range(self.num_per_sram_row)] for j in range(self.npu_num)]
            for iNeuron_in_group in range(self.num_per_sram_row):
                act_id = src_id * self.num_per_sram_row + iNeuron_in_group
                for dst_id, weight_value in self.connection_matrix[act_id].items():
                    weight_value = self.trans_type[self._dtype](weight_value)
                    dst_Npu = dst_id // self.nNeuron_per_Npu
                    dst_id_local = dst_id - dst_Npu * self.nNeuron_per_Npu  # 
                    if self._dtype == "fp32":
                        dst_Tile = dst_id // self.nNeuron_per_tile
                        dst_id_local = dst_id - dst_Tile * self.nNeuron_per_tile  # 
                    tmp_dict_list[dst_Npu][iNeuron_in_group][dst_id_local] = weight_value
            tmp_dict_list = self.mix_dict(self.num_per_sram_row, tmp_dict_list)
            sub = self.num_per_sram_row - 1
            for iNpu in range(self.npu_num):
                tmp_dict = tmp_dict_list[iNpu]
                key = list(tmp_dict[0].keys())
                for col in range(len(key)):
                    data_list = [key[col], 0,
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[sub - i][key[col]] * int(src_id < self.ex_num) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),

                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i][key[col]] * (1 - int(src_id < self.ex_num)) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),
                                0, 0, 0, 0]
                    self.weight_write_list[iNpu].append(data_list)
                    self.weight_source_list[iNpu].append(act_id)
                self.index_suffix[iNpu].append(len(key))
            
    def transform_sp1_b2(self):
        self.num_per_sram_row = self.ncu_state[self._dtype]["row"] * self.base
        for src_id in range(int(self.total_num // self.num_per_sram_row)):
            tmp_dict_list = [[{} for i in range(self.num_per_sram_row)] for j in range(self.npu_num)]
            for iNeuron_in_group in range(self.num_per_sram_row):
                for dst_id_local, weight_value in self.connection_matrix[src_id * self.num_per_sram_row + iNeuron_in_group].items():
                    weight_value = self.trans_type[self._dtype](weight_value)
                    dst_Npu = dst_id_local // self.nNeuron_per_Npu
                    dst_id_local = dst_id_local - dst_Npu * self.nNeuron_per_Npu  # 
                    tmp_dict_list[dst_Npu][iNeuron_in_group][dst_id_local] = weight_value
            tmp_dict_list = self.mix_dict(self.num_per_sram_row, tmp_dict_list)
            sub = self.num_per_sram_row // 2 - 1
            for dst_Npu in range(self.npu_num):
                tmp_dict = tmp_dict_list[dst_Npu]
                key = list(tmp_dict[0].keys())
                for col in range(len(key)):
                    data_list = [key[col], 0, 0,
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i + self.num_per_sram_row // 2][key[col]] * int(src_id < self.ex_num) << (self.num_per_sram_row // 2 - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row // 2)]),
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i + self.num_per_sram_row // 2][key[col]] * (1 - int(src_id < self.ex_num)) << (self.num_per_sram_row // 2 - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row // 2)]),
                                0, 
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[sub - i][key[col]] * int(src_id < self.ex_num) << (self.num_per_sram_row // 2 - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(0, self.num_per_sram_row // 2)]),
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i][key[col]] * (1 - int(src_id < self.ex_num)) << (self.num_per_sram_row // 2 - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(0, self.num_per_sram_row // 2)])]

                    self.weight_write_list[dst_Npu].append(data_list)    
                self.index_suffix[dst_Npu].append(len(key))
                
    def transform_sp2_b1(self):
        self.num_per_sram_row = self.ncu_state[self._dtype]["row"] * self.base
        for src_id in range(int(self.total_num // self.num_per_sram_row)):
            tmp_dict_list = [[{} for i in range(self.num_per_sram_row)] for j in range(self.npu_num)]
            for ids in range(self.num_per_sram_row):
                for dst_id, weight_value in self.connection_matrix[src_id * self.num_per_sram_row + ids].items():
                    weight_value = self.trans_type[self._dtype](weight_value)
                    part = dst_id // self.nNeuron_per_Npu
                    dst_id = dst_id - part * self.nNeuron_per_Npu  # 
                    tmp_dict_list[part][ids][dst_id] = weight_value
            tmp_dict_list = self.mix_dict(self.num_per_sram_row, tmp_dict_list)
            sub = self.num_per_sram_row - 1
            for part in range(self.npu_num):
                tmp_dict = tmp_dict_list[part]
                key = list(tmp_dict[0].keys())  
                for col in range(len(key) // 2):
                    data_list = [key[col * 2] , 0,
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[sub - i][key[col * 2]] * int(src_id < self.ex_num) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i][key[col * 2]] * (1 - int(src_id < self.ex_num)) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),
                                key[col * 2 + 1], 0,
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i][key[col * 2 + 1]] * int(src_id < self.ex_num) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i][key[col * 2 * 1]] * (1 - int(src_id < self.ex_num)) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)])]
                    self.weight_write_list[part].append(data_list)
                if len(key) % 2 == 0:
                    self.index_suffix[part].append(len(key) // 2)
                else:
                    data_list = [key[-1] , 0,
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[sub - i][key[-1]] * int(src_id < self.ex_num) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i][key[-1]] * (1 - int(src_id < self.ex_num)) << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                for i in range(self.num_per_sram_row)]),
                                0, 0, 0, 0]
                    self.weight_write_list[part].append(data_list)
                    self.index_suffix[part].append(len(key) // 2 + 1)
                    
    def transform_sp2_b2(self):
        self.num_per_sram_row = self.ncu_state[self._dtype]["row"] * self.base
        for iGroup in range(int(self.total_num // self.num_per_sram_row)):
            tmp_dict_list = [[{} for i in range(self.num_per_sram_row)] for j in range(self.npu_num)]
            for iNeuron_in_group in range(self.num_per_sram_row):
                act_id = iGroup * self.num_per_sram_row + iNeuron_in_group
                for dst_id_local, weight_value in self.connection_matrix[act_id].items():
                    weight_value = self.trans_type[self._dtype](weight_value)
                    dst_Npu = dst_id_local // self.nNeuron_per_Npu
                    dst_id_local = dst_id_local - dst_Npu * self.nNeuron_per_Npu  # 
                    tmp_dict_list[dst_Npu][iNeuron_in_group][dst_id_local] = weight_value
            tmp_dict_list = self.mix_dict(self.num_per_sram_row, tmp_dict_list)
            half_num = self.num_per_sram_row // 2
            sub = half_num - 1
            for dst_Npu in range(self.npu_num):
                tmp_dict = tmp_dict_list[dst_Npu]
                iNeuron_dst = list(tmp_dict[0].keys())  
                nRow = len(iNeuron_dst) // 2
                iRow = 0
                for iRow in range(nRow): 
                    data_list = [iNeuron_dst[iRow * 2], 0,
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i + half_num][iNeuron_dst[iRow * 2]] << (half_num - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(half_num)]),
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[sub - i][iNeuron_dst[iRow * 2]] << (half_num - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(half_num)]),
                                iNeuron_dst[iRow * 2 + 1], 0, 
                                reduce(lambda x, y : x + y,
                                [tmp_dict[sub - i + half_num][iNeuron_dst[iRow * 2 + 1]] << (half_num - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(half_num)]),
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[sub - i][iNeuron_dst[iRow * 2 + 1]] << (half_num - 1 - i) * 8 * 8 // self.num_per_sram_row
                                for i in range(half_num)])]
                    self.weight_write_list[dst_Npu].append(data_list)
                    self.weight_source_list[dst_Npu].append(act_id)
                if len(iNeuron_dst) % 2 == 0:
                    self.index_suffix[dst_Npu].append(nRow)
                else:
                    #if nConn not even need to add one half row
                    data_list = [iNeuron_dst[iRow * 2], 0,
                                reduce(lambda x, y : x + y, 
                                [tmp_dict[i][iNeuron_dst[iRow * 2]] * int(iGroup < self.ex_num) << (half_num - 1 - i) * 8 
                                for i in range(half_num)]),
                                
                                reduce(lambda x, y : x + y,
                                [tmp_dict[i][iNeuron_dst[iRow * 2]] * (1 - int(iGroup < self.ex_num)) << (self.num_per_sram_row - 1 - i) * 8
                                for i in range(half_num, self.num_per_sram_row)]),
                                0, 0, 0, 0]
                    self.weight_write_list[dst_Npu].append(data_list)
                    self.weight_source_list[dst_Npu].append(act_id)
                    self.index_suffix[dst_Npu].append(nRow + 1)
    
    def transform_sp4_b1(self):
        self.num_per_sram_row = self.ncu_state[self._dtype]["row"] * self.base
        for src_id in range(int(self.total_num // self.num_per_sram_row)):
            tmp_dict_list = [[{} for i in range(self.num_per_sram_row)] for j in range(self.npu_num)]
            for ids in range(self.num_per_sram_row):
                for dst_id, weight_value in self.connection_matrix[src_id * self.num_per_sram_row + ids].items():
                    weight_value = self.trans_type[self._dtype](weight_value)
                    part = dst_id // self.nNeuron_per_Npu
                    dst_id = dst_id - part * self.nNeuron_per_Npu  
                    tmp_dict_list[part][ids][dst_id] = weight_value
            tmp_dict_list = self.mix_dict(self.num_per_sram_row, tmp_dict_list)
            sub = self.num_per_sram_row - 1
            for part in range(self.npu_num):
                tmp_dict = tmp_dict_list[part]
                key = list(tmp_dict[0].keys())  
                for col in range(len(key) // 4):
                    data_list = []
                    for item in range(4):
                        data_list.extend([key[col * 4 + item], 
                                        reduce(lambda x, y : x + y, 
                                        [tmp_dict[sub - i][key[col * 4 + item]] << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                        for i in range(self.num_per_sram_row)])])
                    self.weight_write_list[part].append(data_list)
                if len(key) % 4 == 0:
                    self.index_suffix[part].append(len(key) // 4)
                else:
                    res = len(key) % 4
                    data_list = []
                    for item in range(res):
                        # data_list += [key[-res + item]], [tmp_dict[sub - i][key[-res + item]] for i in range(self.num_per_sram_row)]
                        data_list.extend([key[-res + item], 
                                        reduce(lambda x, y : x + y, 
                                        [tmp_dict[sub - i][key[-res + item]] << (self.num_per_sram_row - 1 - i) * 8 * 4 // self.num_per_sram_row
                                        for i in range(self.num_per_sram_row)])])
                    data_list.extend([0] * (4 - res) * 2)
                    self.weight_write_list[part].append(data_list)
                    self.index_suffix[part].append(len(key) // 4 + 1)