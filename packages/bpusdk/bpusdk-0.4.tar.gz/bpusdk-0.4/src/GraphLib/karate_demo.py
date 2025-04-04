import torch
import torch.nn as nn
from torch.nn.parameter import Parameter
import numpy as np
import sys
import os
from torch_geometric.data import Data
import pandas as pd
import re 

def create_features(graph_node):
    if type(graph_node) is dict:
        node_size = len(graph_node.keys())
        X_1 = torch.eye(node_size)
        return X_1
    else:
        raise ValueError("Graph_node must be a dict or a Data object")

def create_adjacency_matrix(edges):
    nodel_size = 1+torch.max(edges)
    # I_matrix = torch.eye(nodel_size)
    I_matrix = torch.zeros([nodel_size, nodel_size])
    A_matrix = I_matrix.clone()
    for edge in edges:
        A_matrix[edge[0], edge[1]] = 1
        A_matrix[edge[1], edge[0]] = 1
    return A_matrix

def label_create(graph_node):
    if type(graph_node) is dict:
        node_size = len(graph_node.keys())
        labels = torch.zeros(node_size, 1)
        train_mask = torch.tensor(node_size*[False])
        for i, node in enumerate(graph_node.keys()):
            if graph_node[node]['role'] in ['Administrator', 'Instructor']:
                train_mask[i] = True
            if graph_node[node]['community'] == 'Administrator':
                labels[i] = 1
        return labels, train_mask
    else:
        raise ValueError("Graph_node must be a dict or a Data object")

def dataset_loader(data_path):
    attributes = pd.read_csv(os.path.join(data_path, 'attributes.csv'), index_col=['node'])
    attributes_values = {a:{'role':b[0],'community':b[1]} for a,b in enumerate(attributes.values)}
    nodes_features = create_features(attributes_values)
    labels, train_mask = label_create(attributes_values)
    edges = pd.read_csv(os.path.join(data_path, 'edges.csv'))
    edges_values = torch.tensor(np.concatenate((edges.values, edges.values[:,::-1])))
    A_matrix = create_adjacency_matrix(edges_values)
    graph=Data(x=nodes_features, edge_index=edges_values.t().contiguous(), edge_attr=A_matrix,
                y=labels, train_mask=train_mask)
    X_train, Y_train, X_test, Y_test=[], [], [], []
    for index in range(graph.train_mask.shape[0]):
        is_train = graph.train_mask[index]
        if is_train:
            X_train.append(index)
            Y_train.append(graph.y[index].long())
        # else:
        #     X_test.append(index)
        #     Y_test.append(graph.y[index].long())
        X_test.append(index)
        Y_test.append(graph.y[index].long())
    
    return dict(
        graph=graph,
        train_dataset={'input':X_train, 'label':Y_train},
        test_dataset={'input':X_test, 'label':Y_test},
    )


class GCN_Karate():
    def __init__(self, gcn_model_path, graph_data_path):
        gcn_model_path = os.path.join(gcn_model_path, 'model.pt')
        sys.path.append("/".join(gcn_model_path.split('/')[:-1]))
        self.gcn_model_path = gcn_model_path
        self.graph_data_path = graph_data_path
        self.model_load()
        self.data_load()
        if self.node_features.shape[0]!=self.adj_matrix.shape[0]:
            raise ValueError("Node features and adjacency matrix must have the same shape!")

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
        graph_data = dataset_loader(self.graph_data_path)['graph']
        self.node_features = np.array(graph_data.x, dtype=np.float32)
        self.adj_matrix = np.array(graph_data.edge_attr, dtype=np.int32)


if __name__ == '__main__':
    DATA_PATH = '/root/git/Graph_2D_mesh/data/karate'
    MODEL_PATH = '/root/git/Graph_2D_mesh/norm/karate'
    GCN_karate_handle = GCN_Karate(MODEL_PATH, DATA_PATH)
    # print(GCN_karate_handle.Conv_weights)
    print("node_features:\n", GCN_karate_handle.node_features, "\nshape:", GCN_karate_handle.node_features.shape)
    print("adj_matrix:\n", GCN_karate_handle.adj_matrix, "\nshape:", GCN_karate_handle.adj_matrix.shape)