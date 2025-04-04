#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Yukun Feng
# @Date: 2024-05-20

import os
import pickle
import subprocess
import time
import warnings
from pathlib import Path

import numpy as np
import yaml
from loguru import logger

from BrainpyLib.BrainpyBase import BrainpyBase
from BrainpyLib.Common import SpikeWriter, div_round_up
from Mapping.Router import Router40nm
from Mapping.lb2_weight import Weight40nm
from SNNCompiler.lb1_Compiler import lb1_Compiler


class Debug():
    def __init__(self) -> None:
        self.log_running_time = {}

    def record_running_time(self, time_cost, label):
        logger.info(
            f'{label} finished. Time cost: {time_cost:.2f} s')
        self.log_running_time[label] = time_cost


class SNN40nm():
    def __init__(self, network, inpS, inpE, config_file) -> None:
        self.debug = Debug()
        self.inpS = inpS
        self.inpE = inpE
        self.network = network

        self.neuron_scale = network.neuron_scale

        # load config
        config_file = Path(config_file)
        with open(config_file, 'r', encoding='utf8') as stream:
            self.config = yaml.safe_load(stream)

        # Init BpuSetBrainpy
        t0 = time.time()
        bpbase = BrainpyBase(network=network, inpE=inpE, config=self.config)
        self.netbase = bpbase
        self.V_init = bpbase.Vinit
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
        weight = Weight40nm(self.connection_matrix,
                            self.neuron_num, self.neuron_scale, self.V_init, self.config)
        weight.write_to_bin(download_dir)
        t1 = time.time()

        self.debug.record_running_time(t1-t0, label='Weight bin data')

        # spike data dump
        # spike_dir = Path(download_dir) / "spike_bin"
        # spike_dir.mkdir(parents=True, exist_ok=True)
        # np.save(spike_dir / 'X.npy', self.spike_in)
        # SpikeWriter.spike_npy_to_bin(
        #     spike_dir, download_dir, filetype=self.config['FileType'], max_bin_size=4096)
        SpikeWriter.spike_data_to_bin(
            self.inpS, 1, download_dir, filetype=self.config['FileType'], max_bin_size=4096)
        t2 = time.time()
        self.debug.record_running_time(t2-t1, label='Spike bin data')

        # hardware config
        compiler = lb1_Compiler(
            self.config, self.neuron_num, self.netbase, self.network)
        compiler.write_to_bin(download_dir)
        t3 = time.time()
        self.debug.record_running_time(t3-t2, label='Compiler bin data')

        # route data dump
        router = Router40nm(self.config, self.neuron_num)
        router.gen_routing(self.connection_matrix)
        router.write_to_bin(download_dir)
        t4 = time.time()
        self.debug.record_running_time(t4-t3, label='Route bin data')

        logger.info(f'All HW data finished.')


class ASIC_SNN(SNN40nm):
    def __init__(self, network, inpS, inpE, config_file) -> None:
        super().__init__(network, inpS, inpE, config_file)
        self.config['IsAsic'] = True
        self.pall_num = 6
        self.start_tile_num = 0
        self.ex_sp = 0
        self.hw_type = 0 
        self.reset = 1
        self.neu_chip = 16384
        self.sender_path = "../sender/gdiist_host/zcu102_sender"
        self.sender_rst_path = "../sender/sh/load.sh"
        self.xdma = 'xdma0'

    def deploy(self, loadPath, uploadPath) -> int:
        self.tile_num = self.used_tile_num
        self.row = self.used_tile_rows
        self.col = self.used_tile_cols
        self.loadPath = loadPath
        self.uploadPath = uploadPath
        result = 0

        shell_command0 = f"sudo -E sh {self.sender_rst_path}"
        print(shell_command0)
        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command0, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process.wait()
        if process.returncode == 0:
            print("sender_rst执行成功")
        else:
            result = process.returncode
            print(f"sender_rst执行失败, 返回码: {process.returncode}")

        # call 1:a zcu102_sender
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num reset step_start step_count neu_chip xdma
        shell_command1 = f"sudo -E -S {self.sender_path} {self.pall_num} {self.tile_num} {self.start_tile_num} {self.loadPath} {self.uploadPath} {self.row} {self.col} 0 0 {self.hw_type} 0 {self.reset} 0 0 0 {self.xdma}"
        print(shell_command1)  # 输出

        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command1, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process.wait()
        if process.returncode == 0:
            print("1:a zcu102_sender执行成功")  # 输出
        else:
            result = process.returncode
            print(f"1:a zcu102_sender执行失败, 返回码: {process.returncode}")  # 输出
        return result

    def simu(self, step_num) -> int:
        self.start_step = 1
        self.step_num = step_num
        result = 0
        # create dir
        for i in range(0, self.step_num + 1):
            os.makedirs(f'{self.uploadPath}/step' + str(i) +
                        '/spike_check', exist_ok=True)
            os.makedirs(f'{self.uploadPath}/step' + str(i) +
                        '/weight_check', exist_ok=True)
            
        # call 2:a zcu102_sender
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num reset step_start step_count neu_chip xdma
        shell_command2 = f"sudo -E -S {self.sender_path} {self.pall_num} {self.tile_num} {self.start_tile_num} {self.loadPath} {self.uploadPath} {self.row} {self.col} {self.ex_sp} 1 {self.hw_type} 1 {self.reset} {self.start_step} {self.step_num} {self.neu_chip} {self.xdma}"
        print(shell_command2)  # 输出

        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command2, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')  # 输出
        process.wait()
        if process.returncode == 0:
            print("2:a zcu102_sender执行成功")  # 输出
        else:
            result = process.returncode
            print(f"2:a zcu102_sender执行失败, 返回码: {process.returncode}")  # 输出
        return result

    def rw_test(self, loadPath, uploadPath) -> int:
        self.tile_num = self.used_tile_num
        self.row = self.used_tile_rows
        self.col = self.used_tile_cols
        self.loadPath = loadPath
        self.uploadPath = uploadPath
        
        result = 0
        # create dir
        os.makedirs(f'{self.uploadPath}/step' + str(0) +
                    '/weight_check', exist_ok=True)

        shell_command0 = f"sudo -E sh {self.sender_rst_path}"
        print(shell_command0)
        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command0, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process.wait()
        if process.returncode == 0:
            print("sender_rst执行成功")
        else:
            result = process.returncode
            print(f"sender_rst执行失败, 返回码: {process.returncode}")

        # call 1:a zcu102_sender
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num reset step_start step_count neu_chip xdma
        shell_command1 = f"sudo -E -S {self.sender_path} {self.pall_num} {self.tile_num} {self.start_tile_num} {self.loadPath} {self.uploadPath} {self.row} {self.col} 0 2 {self.hw_type} 1 {self.reset} 1 1 {self.neu_chip} {self.xdma}"
        print(shell_command1)  # 输出

        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command1, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')  # 输出
        process.wait()
        if process.returncode == 0:
            print("1:a zcu102_sender执行成功")  # 输出
        else:
            result = process.returncode
            print(f"1:a zcu102_sender执行失败, 返回码: {process.returncode}")  # 输出
        return result
    
    def run_single_chip(self, step_num, mode, upload_dir, reset=True):
        if mode != 0 and mode != 1 and mode != 2:
            print("Unsupported mode")
            exit()

        print(f"------START----------")
        sender_rst_path = "./shell/sender_rst.sh"
        reset_asic_path = "./shell/rst_asic.sh"

        tile_num = self.used_tile_num
        row = self.used_tile_rows
        col = self.used_tile_cols
        pall_num = 1
        start_tile_num = 0
        bandwidth = min(self.neuron_num, 16384) if mode != 0 else 0
        zcu102_sender_path = "./shell/zcu102_sender_spike" if mode != 2 else "./shell/zcu102_sender_weight"
        download_dir = self.download_dir

        # create dir
        if os.path.exists(upload_dir) == False:
            res_path = f"{upload_dir}"
            os.mkdir(res_path)

        for i in range(1, step_num+1):
            step_path = f"{upload_dir}/step{i}"
            if os.path.exists(step_path) == False:
                os.mkdir(step_path)

                spike_check_path = f"{upload_dir}/step{i}/spike_check"
                os.mkdir(spike_check_path)

                weight_check_path = f"{upload_dir}/step{i}/weight_check"
                os.mkdir(weight_check_path)

        if reset == True and mode != 0:
            # call reset_asic
            shell_command = f"{reset_asic_path}"
            print(shell_command)
            echo = subprocess.Popen(
                ['echo', '123456788'], stdout=subprocess.PIPE)
            process = subprocess.Popen(shell_command, shell=True, stdin=echo.stdout,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            process.wait()
            if process.returncode == 0:
                print("reset_asic执行成功")
            else:
                print(f"reset_asic执行失败, 返回码: {process.returncode}")

        # TODO: call sender_rst
        shell_command0 = f"sudo -E -S sh {sender_rst_path}"
        print(shell_command0)
        echo = subprocess.Popen(['echo', '123456788'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command0, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process.wait()
        if process.returncode == 0:
            print("sender_rst执行成功")
        else:
            print(f"sender_rst执行失败, 返回码: {process.returncode}")

        # call 1:a zcu102_sender // Downloading
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num step_count neu_chip
        shell_command1 = f"sudo -E -S {zcu102_sender_path} {pall_num} {tile_num} {start_tile_num} {download_dir} {upload_dir} {row} {col} 0 0 0 0 0 0"
        print(shell_command1)
        echo = subprocess.Popen(['echo', '123456788'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command1, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process.wait()
        if process.returncode == 0:
            print("1:a zcu102_sender执行成功")
        else:
            print(f"1:a zcu102_sender执行失败, 返回码: {process.returncode}")

        # call 2:a zcu102_sender // Runtime
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num step_count neu_chip
        shell_command2 = f"sudo -E -S {zcu102_sender_path} {pall_num} {tile_num} {start_tile_num} {download_dir} {upload_dir} {row} {col} 1 1 0 1 {step_num} {bandwidth}"
        print(shell_command2)

        echo = subprocess.Popen(['echo', '123456788'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command2, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')
        process.wait()
        if process.returncode == 0:
            print("2:a zcu102_sender执行成功")
        else:
            print(f"2:a zcu102_sender执行失败, 返回码: {process.returncode}")

        print(f"neuron_num: {int(self.neuron_num/1024)} K")
        print(f"mode: {mode}")
        print(f"{shell_command0}")
        print(f"{shell_command1}")
        print(f"{shell_command2}")

    def run_multi_chips(self, step_num, mode, upload_dir, reset=True):
        reset = int(reset)
        if mode != 0 and mode != 1 and mode != 2:
            print("Unsupported mode")
            exit()

        print(f"------START----------")  # 输出
        tile_num = self.used_tile_num
        row = self.used_tile_rows
        col = self.used_tile_cols
        pall_num = 1
        start_step = 1
        start_tile_num = 0
        bandwidth = min(self.neuron_num, 16384) if mode != 0 else 0
        zcu102_sender_path = "./shell/zcu102_sender_new"
        download_dir = self.download_dir
        # download_dir = "/home/ws_0803/work/data/ei_data_16k_0.5"

        # create dir
        if os.path.exists(upload_dir) == False:
            res_path = f"{upload_dir}"
            os.mkdir(res_path)

        for i in range(1, step_num+1):
            step_path = f"{upload_dir}/step{i}"
            if os.path.exists(step_path) == False:
                os.mkdir(step_path)

                spike_check_path = f"{upload_dir}/step{i}/spike_check"
                os.mkdir(spike_check_path)

                weight_check_path = f"{upload_dir}/step{i}/weight_check"
                os.mkdir(weight_check_path)

        # call 1:a zcu102_sender
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num step_count neu_chip
        shell_command1 = f"sudo -E -S {zcu102_sender_path} {pall_num} {tile_num} {start_tile_num} {download_dir} {upload_dir} {row} {col} 0 0 0 0 {reset} 0 0 0"
        print(shell_command1)  # 输出

        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command1, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process.wait()
        if process.returncode == 0:
            print("1:a zcu102_sender执行成功")  # 输出
        else:
            print(f"1:a zcu102_sender执行失败, 返回码: {process.returncode}")  # 输出

        # call 2:a zcu102_sender
        # pall_num total_tile_num start_tile_num downloadPath uploadPath  row col extern_sp  mode  hw_type sample_num step_count neu_chip
        shell_command2 = f"sudo -E -S {zcu102_sender_path} {pall_num} {tile_num} {start_tile_num} {download_dir} {upload_dir} {row} {col} 1 1 0 1 {reset} {start_step} {step_num} {bandwidth}"
        print(shell_command2)  # 输出

        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command2, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')  # 输出
        process.wait()
        if process.returncode == 0:
            print("2:a zcu102_sender执行成功")  # 输出
        else:
            print(f"2:a zcu102_sender执行失败, 返回码: {process.returncode}")  # 输出

        print(f"neuron_num: {self.neuron_num/1024} K")  # 输出
        # print(f"mode: {mode}")
        # print(f"{shell_command1}")
        # print(f"{shell_command2}")


class FPGA_SNN(SNN40nm):
    def __init__(self, network, spike_in, config_file) -> None:
        super().__init__(network, spike_in, config_file)
        self.config['IsAsic'] = False

    def run(self, step_num, upload_dir):
        # self.download_dir = "/home/node50/work/data/ei_data_16k_0.5"
        exe_path = "./run_ei.sh"
        # create dir
        if os.path.exists(upload_dir) == False:
            res_path = f"{upload_dir}"
            os.mkdir(res_path)

        for i in range(0, step_num+1):
            step_path = f"{upload_dir}/step{i}"
            if os.path.exists(step_path) == False:
                os.mkdir(step_path)

                spike_check_path = f"{upload_dir}/step{i}/spike_check"
                os.mkdir(spike_check_path)

                weight_check_path = f"{upload_dir}/step{i}/weight_check"
                os.mkdir(weight_check_path)

        # sudo -E sh ./run_ei.sh /home/node50/work/data/ei_data_16k_0.5 /home/upload/ei_16 100 16384
        shell_command0 = f"sudo -E -S sh {exe_path} {self.download_dir} {upload_dir} {step_num} {self.neuron_num}"
        echo = subprocess.Popen(['echo', 'gdiist@123'], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command0, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')

        process.wait()
        if process.returncode == 0:
            print("exe执行成功")
        else:
            print(f"exe执行失败, 返回码: {process.returncode}")
        # call(download_dir,upload_dir,T,self.neuron_num,self.cols,self.cols)

