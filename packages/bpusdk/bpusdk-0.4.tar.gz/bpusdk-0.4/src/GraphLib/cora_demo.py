import os 
import torch
import pandas as pd
import numpy as np
import re
import sys

class GCN_Cora():
    def __init__(self, gcn_model_path, graph_data_path):
        sys.path.append("/".join(gcn_model_path.split('/')[:-1]))
        self.gcn_model_path = gcn_model_path
        self.graph_data_path = graph_data_path
        self.model_load()
        self.data_load()

    def model_load(self):
        GCN_model = torch.load(self.gcn_model_path)
        GCN_parameters = GCN_model.state_dict()
        GCN_architectur = [x for x in GCN_model.named_children()] 
        Conv_lenght = len([layer for layer in GCN_architectur if 'layer' in layer[0]])
        self.Conv_weights = [dict() for _ in range(Conv_lenght)]
        for layer_parameter in GCN_parameters:
            if 'layer' in layer_parameter:
                layer_index = int(re.findall(r"layer(.+?)\.", layer_parameter)[0])
                assert layer_index<=Conv_lenght, "Error: model layer index out of range"
                layer_name = re.findall(r"layer.*\.(.+)$", layer_parameter)
                self.Conv_weights[layer_index-1][layer_name[0]] = GCN_parameters[layer_parameter]

    def data_load(self):
        raw_data = pd.read_csv(os.path.join(self.graph_data_path, 'cora.content'), sep = '\t',header = None)
        num = raw_data.shape[0] # 样本点数2708
        # 编号映射
        a, b = list(raw_data.index), list(raw_data[0])
        c = zip(b, a)
        map = dict(c)
        # 特征规格化
        features = raw_data.iloc[:,1:-1]
        for c, v in raw_data.iloc[:,1:-1].items():
            features.append(list(v))
        self.node_features = np.array(features)
        
        # 连接关系
        raw_data_cites = pd.read_csv(os.path.join(self.graph_data_path, 'cora.cites'), sep = '\t',header = None)
        matrix = np.zeros((num,num))
        # 创建邻接矩阵
        for i ,j in zip(raw_data_cites[0],raw_data_cites[1]):
            x = map[i] ; y = map[j]  # 替换论文编号为[0,2707]
            matrix[x][y] = matrix[y][x] = 1 # 有引用关系的样本点之间取1
        for i in range(num):
            matrix[i][i] = 1         # 自连接
        self.adj_matrix = matrix


