#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Yukun Feng
# @Date: 2024-06-19

import time
from pathlib import Path

import numpy as np
import yaml
from loguru import logger

from util.BrainpyBase import BrainpyBase
from Common.Common import SpikeWriter, div_round_up
from Mapping.Router import lb2_Router
from Mapping.lb2_weight import lb2_Weight
from SNNCompiler.lb1_Compiler import Compiler28nmSNN


class Debug():
    def __init__(self) -> None:
        self.log_running_time = {}

    def record_running_time(self, time_cost, label):
        logger.info(
            f'{label} finished. Time cost: {time_cost:.2f} s')
        self.log_running_time[label] = time_cost


class Graph28nm():
    def __init__(self, network, spike_in, config_file) -> None:
        self.debug = Debug()
        self.spike_in = spike_in
        self.network = network

        self.neuron_scale = network.neuron_scale

        # load config
        config_file = Path(config_file)
        with open(config_file, 'r', encoding='utf8') as stream:
            self.config = yaml.safe_load(stream)

        # Init BpuSetBrainpy
        t0 = time.time()
        bpbase = BrainpyBase(network)
        self.neuron_num = bpbase.get_neuron_num()
        self.connection_matrix = bpbase.get_connection_matrix()
        t1 = time.time()
        self.debug.record_running_time(t1-t0, label='Network analysis')

        self.used_tile_num = int(np.ceil(
            self.neuron_num/(self.config['Tile_NpuNum']*self.config['Npu_NeuronNum'])))
        self.used_tile_cols = div_round_up(
            self.used_tile_num, self.config['Y_TileNum'])
        self.used_tile_rows = self.used_tile_num if self.used_tile_cols == 1 else self.config[
            'X_TileNum']
        logger.info(
            f"Used tile num: {self.used_tile_num}, rows: {self.used_tile_rows}, cols: {self.used_tile_cols}")

    def gen_bin_data(self, download_dir):
        self.config['FileType'] = 'bin'

        # weight data dump
        t0 = time.time()
        weight = lb2_Weight(self.connection_matrix,
                            self.neuron_num, self.neuron_scale, self.config)
        weight.write_to_bin(download_dir)
        t1 = time.time()

        self.debug.record_running_time(t1-t0, label='Weight bin data')

        # spike data dump
        SpikeWriter.spike_data_to_bin(
            self.spike_in, 1, download_dir, filetype=self.config['FileType'], max_bin_size=4096)
        t2 = time.time()
        self.debug.record_running_time(t2-t1, label='Spike bin data')

        # hardware config
        compiler = Compiler28nmSNN(self.config, self.neuron_num, self.network)
        compiler.write_to_bin(download_dir)
        t3 = time.time()
        self.debug.record_running_time(t3-t2, label='Compiler bin data')

        # route data dump
        router = lb2_Router(self.config, self.neuron_num)
        router.gen_routing(self.connection_matrix)
        router.write_to_bin(download_dir)
        t4 = time.time()
        self.debug.record_running_time(t4-t3, label='Route bin data')

        logger.info(f'All bin data finished.')

    def run(self, step_num, mode, upload_dir, reset=True):
        pass
