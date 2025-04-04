import os
import torch
import re
import json
import numpy as np
import pandas as pd
import argparse
from loguru import logger
import sys
from Graph.GNN.cora_demo import GCN_Cora
from Graph.GNN.karate_demo import GCN_Karate
from Graph.GNN.gcn_weight import Weight28nm


class Debug():
    def __init__(self) -> None:
        self.log_running_time = {}

    def record_running_time(self, time_cost, label):
        logger.info(
            f'{label} finished. Time cost: {time_cost:.2f} s')
        self.log_running_time[label] = time_cost
        

class GCN28nm():
    def __init__(self, args):
        self.debug = Debug()
        self.args = args
        if self.args.demo_type == "cora":
            self.Graph_info = GCN_Cora(args.gcn_model_path, args.graph_data_path)
        elif self.args.demo_type == "karate":
            self.Graph_info = GCN_Karate(args.gcn_model_path, args.graph_data_path)
        else:
            raise ValueError("Invalid demo type")

        self.config_28nm = json.load(open(args.BPU_config, 'r'))

    
    def gen_bin_data(self, download_dir):
        weight = Weight28nm(
            Graph_info_dic = {
                "connection_matrix": self.Graph_info.adj_matrix,
                "node_features": self.Graph_info.node_features,
                "GCN_weight": self.Graph_info.Conv_weights
            },
            config_28nm = self.config_28nm
        )
        weight.write_to_bin(download_dir)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--gcn_model_path", type=str, default='/root/git/Graph_2D_mesh/norm/karate', help="GCN model path")
    parser.add_argument("--graph_data_path", type=str, default='/root/git/Graph_2D_mesh/data/karate', help="graph data path")
    parser.add_argument("--BPU_config", type=str, default='./config/config28nm.json', help="BPU config file")
    parser.add_argument("--demo_type", type=str, default='karate', help="demo type")

    args = parser.parse_args()


    
    bpuset = GCN28nm(args=args)
    bpuset.gen_bin_data(download_dir="./bin")
