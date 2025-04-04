import time
import os
from pathlib import Path
import subprocess
import numpy as np
import yaml
from loguru import logger

from BrainpyLib.BrainpyBase import BrainpyBase
from BrainpyLib.Common import SpikeWriter, div_round_up
from Mapping.Router import lb2_Router
from Mapping.lb2_weight import lb2_Weight
from SNNCompiler.lb2_Compiler import Compiler28nmSNN
import math
import json

class lb2_deploy():
    def __init__(self, download_dir, upload_dir,sender_path,sender_rst_path,pwd,id) -> None:
        self.download_dir = download_dir
        self.upload_dir = upload_dir
        self.sender_path = sender_path
        self.sender_rst_path = sender_rst_path
        self.pwd = pwd
        self.id = id
    
    def run(self, step, mode=2, xdma_id=0, reset = False) -> int:
        json_path = self.download_dir + "/config.json"
        with open(json_path, 'r', encoding='utf8') as stream:
            config = json.load(stream)
        x_tileNum = config['nRow']
        y_tileNum = config['nCol']
        nTile = config['nTile']
        Is_Y_First = config['Is_Y_First']
        data_type = config['Dtype']
        neu_base = config['Base']
        weight_spilt = config['Split']
        syn_calcu_tw = config['syn_calcu_tw'] 
        neu_calcu_len = config['neu_calcu_len'] 
        syn_calcu_len = config['syn_calcu_len'] 

        sender_path = self.sender_path
        sender_rst_path = self.sender_rst_path
        result = 0
        if reset:
            shell_command0 = f"sudo -E sh {sender_rst_path} {self.id}"
            print(shell_command0)
            echo = subprocess.Popen(['echo', self.pwd], stdout=subprocess.PIPE)
            process = subprocess.Popen(shell_command0, shell=True, stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            process.wait()
            if process.returncode == 0:
                print(shell_command0)
                print("sender_rst执行成功")
            else:
                result = process.returncode
                print(shell_command0)
                print(f"sender_rst执行失败, 返回码: {process.returncode}")
        
        shell_command1 = f"sudo -E -S {sender_path} {self.download_dir} {self.upload_dir} {mode} {xdma_id} {x_tileNum} {y_tileNum} {nTile} {Is_Y_First} {data_type} {neu_base} {weight_spilt} {syn_calcu_tw} {neu_calcu_len} {syn_calcu_len} {step} 0 1"
        print(shell_command1)  

        echo = subprocess.Popen(['echo', self.pwd], stdout=subprocess.PIPE)
        process = subprocess.Popen(shell_command1, shell=True, stdin=echo.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')  # 输出
        process.wait()
        if process.returncode == 0:
            print(shell_command1)
            print("1:a zcu102_sender执行成功")  
        else:
            result = process.returncode
            print(shell_command1)
            print(f"1:a zcu102_sender执行失败, 返回码: {process.returncode}")  # 输出
        return result

    
