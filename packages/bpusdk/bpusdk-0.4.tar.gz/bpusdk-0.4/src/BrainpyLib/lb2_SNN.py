import time
from pathlib import Path
import yaml
from loguru import logger

from BrainpyLib.BrainpyBase import BrainpyBase
from BrainpyLib.Common import SpikeWriter
from Mapping.Router import lb2_Router
from Mapping.lb2_weight import lb2_Weight
from SNNCompiler.lb2_Compiler import Compiler28nmSNN
import math
import json

class Debug():
    def __init__(self) -> None:
        self.log_running_time = {}

    def record_running_time(self, time_cost, label):
        logger.info(
            f'{label} finished. Time cost: {time_cost:.2f} s')
        self.log_running_time[label] = time_cost


class lb2_SNN():
    def __init__(self, network, inpS, inpE, config_file,mode=0) -> None:
        self.debug = Debug()
        self.spike_in = inpS
        self.network = network
        self.neuron_scale = network.neuron_scale
        self.mode = mode

        # load config
        config_file = Path(config_file)
        with open(config_file, 'r', encoding='utf8') as stream:
            self.config = yaml.safe_load(stream)

        # Init BpuSetBrainpy
        t0 = time.time()
        bpbase = BrainpyBase(network=network, inpE=inpE, config=self.config)
        self.bpbase = bpbase
        self.V_init = bpbase.Vinit
        
        self.neuron_num = bpbase.get_neuron_num()
        self.connection_matrix = bpbase.get_connection_matrix()
        
        t1 = time.time()
        self.debug.record_running_time(t1-t0, label='Network analysis')

        if self.config['Npu_NeuronNum'] == 'auto':
            dType2scale = {"fp32":1,"fp16":2,"int16":2,"int8":4}
            self.config['Npu_NeuronNum'] = 4096*dType2scale[self.config['Dtype']] * self.config['Base']

        nNeuron_per_tile = self.config['Npu_NeuronNum'] * self.config['Tile_NpuNum']
        self.config['nTile'] = math.ceil(self.neuron_num/nNeuron_per_tile)
        self.config['nRow'] = math.ceil(self.config['nTile']/self.config['X_TileNum'])         
        self.config['nCol'] = self.config['nTile'] if self.config['nRow'] == 1 else self.config['X_TileNum']
        logger.info(f"Used tile num: {self.config['nTile']}, rows: {self.config['nRow']}, cols: {self.config['nCol']}")

    def gen_bin_data(self, download_dir):
        self.config['FileType'] = 'bin'
        data_dir = Path(download_dir)
        data_dir.mkdir(parents=True, exist_ok=True)
        mode = self.mode

        # weight data dump
        t0 = time.time()
        weight = lb2_Weight(self.connection_matrix,
                            self.neuron_num, self.neuron_scale, self.V_init, self.config,mode=mode)
        weight.write_to_bin(data_dir)
        if self.mode ==2:
            weight.merge_weight(data_dir)
        t1 = time.time()

        self.debug.record_running_time(t1-t0, label='Weight bin data')

        # spike data dump
        # SpikeWriter.spike_data_to_bin(
        #     self.spike_in, 1, data_dir, filetype=self.config['FileType'], max_bin_size=4096)
        t2 = time.time()
        self.debug.record_running_time(t2-t1, label='Spike bin data')

        # hardware config
        compiler= Compiler28nmSNN(self.config, self.neuron_num, self.bpbase)
        compiler.write_to_bin(data_dir)
        t3 = time.time()
        self.debug.record_running_time(t3-t2, label='Compiler bin data')

        # route data dump
        router = lb2_Router(self.config, self.neuron_num,mode=mode)
        router.gen_routing(self.connection_matrix)
        router.write_to_bin(data_dir)
        t4 = time.time()
        self.debug.record_running_time(t4-t3, label='Route bin data')
        logger.info(f'All bin data finished.')

        # Write JSON config 
        dType2scale = {"fp32":0,"fp16":1,"int16":2,"int8":3}
        config_data = {
                "mode": mode,
                "nNeuron": self.bpbase.neuron_num,
                "seed": int(self.bpbase.network.initState[1]),
                "nRow": self.config['nRow'],
                "nCol": self.config['nCol'],
                "nTile": self.config['nTile'],
                "Is_Y_First": int(self.config['Is_Y_First']),
                "Dtype": dType2scale[self.config['Dtype']],
                "Base": self.config['Base']-1,
                "Split": self.config['Split']-1,
                "syn_calcu_tw": weight.syn_calcu_tw,
                "neu_calcu_len": compiler.neu_calcu_len ,
                "syn_calcu_len": compiler.syn_calcu_len ,
                }
        with open(data_dir/"config.json", "w") as json_file:
            json.dump(config_data, json_file, indent=4)
    
        #write log file
        config_log = ["-----------Hardware Config-----------\n"]
        config_log.append(f"Used tile num: {self.config['nTile']}, rows: {self.config['nRow']}, cols: {self.config['nCol']}\n")
        config_log.append(f"Base: {self.config['Base']}, Split: {self.config['Split']}\n")
        config_log.append(f"nNeuron: {self.neuron_num}\n\n")
        
        time_log = ["-----------RunningTime-----------\n"]
        for step in self.debug.log_running_time:
            s = step +": " f"{self.debug.log_running_time[step]:.2g} s\n"
            time_log.append(s)
        time_log.append("\n")
        
        with open(data_dir/"log.txt", "w") as file:
            file.write(" ".join(config_log))
            file.write(" ".join(time_log))
            file.write(" ".join(self.bpbase.log))
            file.write(" ".join(weight.log))
            file.write(" ".join(router.log))
        logger.info(f'log generated.')
        
    def gen_hex_data(self, download_dir):
        self.config['FileType'] = 'hex'
        mode = self.mode

        # weight data dump
        t0 = time.time()
        weight = lb2_Weight(self.connection_matrix,
                            self.neuron_num, self.neuron_scale, self.V_init,self.config,mode=mode)
        weight.write_to_hex(download_dir)
        t1 = time.time()
        self.debug.record_running_time(t1-t0, label='Weight hex data')

        # spike data dump
        # SpikeWriter.spike_data_to_bin(
        #     self.spike_in, 1, download_dir, filetype='hex', max_bin_size=4096)
        t2 = time.time()
        self.debug.record_running_time(t2-t1, label='Spike hex data')

        # # hardware config
        compiler = Compiler28nmSNN(self.config, self.neuron_num, self.bpbase)
        compiler.write_to_hex(download_dir)
        t3 = time.time()
        self.debug.record_running_time(t3-t2, label='Compiler hex data')

        # # route data dump
        router = lb2_Router(self.config, self.neuron_num)
        router.gen_routing(self.connection_matrix)
        router.write_to_bin(download_dir, file_type='hex')
        t4 = time.time()
        self.debug.record_running_time(t4-t2, label='Route hex data')

        logger.info(f'All hex data finished.')
