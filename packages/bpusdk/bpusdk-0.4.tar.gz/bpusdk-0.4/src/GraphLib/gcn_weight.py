import os
import torch
import re
from pathlib import Path
import numpy as np

from Common.Common import Fake, div_round_up, get_hex_data

import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f',f))[0])

def hex_to_float(h):
    return struct.unpack('<f', struct.pack('<I', int(h, 16)))[0]

def hex_to_int(h):
    return int(h, 16)

vectorized_float_to_hex = np.vectorize(float_to_hex)
vectorized_hex_to_float = np.vectorize(hex_to_float)
vectorized_hex_to_int = np.vectorize(hex_to_int)

class Weight28nm():
    def __init__(self, Graph_info_dic, config_28nm):
        if isinstance(Graph_info_dic, dict):
            self.Graph_info_dic = Graph_info_dic
        else:
            raise TypeError("Graph_info_dic must be a dict")
        self.connection_matrix = self.Graph_info_dic.get("connection_matrix", None)
        self.node_features = self.Graph_info_dic.get("node_features", None)
        self.GCN_weight = self.Graph_info_dic.get("GCN_weight", None)
        # if not self.connection_matrix or not self.node_features or not self.GCN_weight:
        if any([self.connection_matrix is None, self.node_features is None, self.GCN_weight is None]):
            raise ValueError("Graph_info_dic has None value")
        
        self.config_28nm = config_28nm
        self.NPU_sram_len = hex(int(self.config_28nm['NPU0_end'],16) - int(self.config_28nm['NPU0_start'],16))

        # print(self.node_features)
        # print(self.connection_matrix)
        # print(self.GCN_weight)

        
    def mem_head(self, **kwargs):
        # layer_num , layer_dim, node_num, weight_addr_len, node_values_len, dst_weight_len, gcn_weight_len
        results = []
        layer_num = len(self.GCN_weight)+1
        layer_dim = [self.node_features.shape[1]] + [self.GCN_weight[i]['bias'].shape[0] for i in range(layer_num-1)]
        
        if self.tmp_file == 1:
            node_num = self.node_features.shape[0]
            men_len = []
            men_len.append(layer_num+2+5)
            for key, value in kwargs.items():
                if key == 'weight_addr_len':
                    assert len(value[0]) == node_num, "Error: weight_addr is failed the verification"
                if key == 'node_values_len':
                    assert len(value[0]) == sum([node_num*dim for dim in layer_dim]), "Error: node_values is failed the verification"
                if key == 'dst_weight_len':
                    assert kwargs['weight_addr_len'][0][-1]*2 == len(value[0]), f"Error: dst_weight is failed the verification"
                if key == 'gcn_weight_len':
                    assert len(value[0]) == sum([layer_dim[layer]*layer_dim[layer+1]+layer_dim[layer+1] for layer in range(layer_num-1)]), "Error: gcn_weight is failed the verification"
                men_len.append(len(value[0]))
            results.append([layer_num]+layer_dim+[node_num]+list(np.cumsum(men_len)))
        else:
            pass
        print("head:\t", results)
        return results

    def weight_addr(self):
        # source节点连接权重的相对地址 
        # id_degree: 每个节点的度数 
        # weight_addr: 每个节点的权重地址 
        results = []
        if self.tmp_file == 1:
            id_degree = [0]*self.connection_matrix.shape[0]
            weight_addr = np.array([])
            for source_id in range(self.connection_matrix.shape[0]):
                id_degree[source_id] = np.sum(self.connection_matrix[source_id,:])
                weight_addr = np.concatenate((weight_addr, np.array([id_degree[source_id]])))
                # for dst_id in range(self.connection_matrix.shape[1]):
                #     if self.connection_matrix[source_id,dst_id] == 1:
                #         weight_addr = np.concatenate((weight_addr, dst_id))
            # results.append(np.tile(np.array(id_degree).astype("<u4"), len(self.GCN_weight)+1))
            results.append(np.cumsum(weight_addr))
        else:
            pass
        print("weight_addr:\t", results)
        return results, id_degree

    def node_values(self):
        # 节点多层特征
        results = []
        if self.tmp_file == 1:
            node_values = np.array([])

            node_feature = np.array(self.node_features).astype("<f4").reshape(-1)
            # placeholder = np.array([0]*(node_feature.shape[0]%2)).astype("<f4")      # 占位填0
            # node_values = np.concatenate((node_values, node_feature, placeholder),axis=0)
            node_values = np.concatenate((node_values, node_feature),axis=0)
            
            layer_dim = [self.GCN_weight[i]['bias'].shape[0] for i in range(len(self.GCN_weight))]
            for dim in layer_dim:
                node_feature = np.array([0]*dim).astype("<f4")
                # placeholder = np.array([0]*(node_feature.shape[0]%2)).astype("<f4")   # 占位填0
                # node_values = np.concatenate((node_values, node_feature, placeholder),axis=0)
                node_values = np.concatenate((node_values, np.tile(node_feature, self.node_features.shape[0])),axis=0)
            node_values = vectorized_float_to_hex(node_values)
            node_values = vectorized_hex_to_int(node_values)
            results.append(node_values)
        else:
            pass
        print("node_values:\t", results)
        return results

    def dst_weight(self, id_degree):
        # source节点连接边dst_id与连接权重
        # [dst_id_1, dst_weight_1, dst_id_2, dst_weight_2]
        results = []
        if self.tmp_file == 1:
            dst_weight = np.array([])
            for source_id in range(self.connection_matrix.shape[0]):
                for dst_id in range(self.connection_matrix.shape[1]):
                    if self.connection_matrix[source_id, dst_id] == 1:
                        value = np.array([1/(np.sqrt(id_degree[source_id])*np.sqrt(id_degree[dst_id]))]).astype("<f4")
                        dst_weight = np.concatenate((dst_weight, np.array([dst_id]), value), axis=0)
            dst_weight = vectorized_float_to_hex(dst_weight)
            dst_weight = vectorized_hex_to_int(dst_weight)
            results.append(dst_weight)
        print("dst_weight:\t", results)
        return results

    def gcn_weight(self):
        # GCN层权重偏置
        results = []
        for ids in range(self.tmp_file):
            weight = np.array([])
            for layer_index in range(len(self.GCN_weight)):
                w = np.array(self.GCN_weight[layer_index]['W'].reshape(-1)).astype("<f4")
                bias = np.array(self.GCN_weight[layer_index]['bias']).astype("<f4")
                # placeholder = np.array([0]*((w.shape[0]+bias.shape[0])%2)).astype("<f4")   # 占位填0
                weight = np.concatenate((weight, w, bias), axis=0)
            weight = vectorized_float_to_hex(weight)
            weight = vectorized_hex_to_int(weight)
            results.append(weight)
        print("gcn_weight:\t", results)
        return results

    def write_to_bin(self, output_dir):
        output_dir = Path(output_dir) / 'weight'
        output_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
        # tmp_file = self.used_chip_num
        self.tmp_file = 1

        # part 1: 节点索引
        weight_addr, id_degree = self.weight_addr()

        # part 2: 节点特征存储
        node_values = self.node_values()

        # part 3: 连接+权重
        dst_weight = self.dst_weight(id_degree)

        # part 4: GCN权重
        gcn_weight = self.gcn_weight()

        # part 5: Sram头
        mem_head = self.mem_head(weight_addr_len=weight_addr, 
                                node_values_len=node_values, 
                                dst_weight_len=dst_weight, 
                                gcn_weight_len=gcn_weight)
    
        for ids in range(self.tmp_file):
            file_path = output_dir / f"weight_{ids}.bin"
            print(file_path)
            file_path.unlink(missing_ok=True)
            if os.path.exists(file_path):
                os.remove(file_path)
            
            file_path.unlink(missing_ok=True)
            Fake.fwrite(file_path=file_path,
                        arr=mem_head[ids], dtype="<u4")
            Fake.fwrite(file_path=file_path,
                        arr=weight_addr[ids], dtype="<u4")
            Fake.fwrite(file_path=file_path,
                        arr=node_values[ids], dtype="<u4")
            Fake.fwrite(file_path=file_path,
                        arr=dst_weight[ids], dtype="<u4")
            Fake.fwrite(file_path=file_path,
                        arr=gcn_weight[ids], dtype="<u4")            

