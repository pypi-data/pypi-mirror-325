"""Network adapter base class
"""
import os
import warnings
from collections import defaultdict
from pathlib import Path
from typing import  Optional
import numpy as np
from loguru import logger
from BrainpyLib.Common import Fake 

import math
warnings.filterwarnings("ignore")

class lb1_Weight():
    def __init__(self, connection_matrix, neuron_num, neuron_scale, V_init, config) -> None:
        self.connection_matrix = connection_matrix
        self.neuron_num = neuron_num

        if neuron_scale > 1 or neuron_scale < 0:
            raise NotImplementedError(
                "Neuron scale is only supported (0, 1.0]")
        else:
            self.neuron_scale = neuron_scale

        self.fanout = 10
        self.V_init = V_init
        self.cfg = config['cfg']
        self.max_neurons_per_npu: int = config['Npu_NeuronNum']
        self.nNpu_layout_per_tile: int = config['Tile_NpuNum']
        self.nNeuron_per_tile = config['Npu_NeuronNum'] * config['Tile_NpuNum']
        self.nTile_layout = math.ceil(neuron_num, self.nNeuron_per_tile)

        if self.cfg == 3:
            self.weight_addr_0: int = 256 * (16 * (self.nTile_layout - 1) + self.nNpu_layout_per_tile) + \
                16 * (self.max_neurons_per_npu * 2 // 8)
        elif self.cfg == 2:
            self.weight_addr_0: int = 256 * (16 * (self.nTile_layout - 1) + self.nNpu_layout_per_tile) + \
                16 * (self.max_neurons_per_npu * 2 // 4)
        else:
            self.weight_addr_0: int = 256 * \
                (16 * (self.nTile_layout - 1) + self.nNpu_layout_per_tile) + \
                16 * (self.max_neurons_per_npu * 2)

    def weight_addr(self):
        fanout = self.fanout
        dst_id_count = []
        results = []

        file_num = self.nTile_layout
        dst_id_count = [[] for _ in range(file_num)]
        for dst_ids in self.connection_matrix.values():
            tmp_list = [[] for _ in range(file_num)]
            for key in dst_ids.keys():
                tmp_list[int(key) // self.nNeuron_per_tile] += [key]

            for i in range(file_num):
                dst_id_count[i] += [len(tmp_list[i])]

        for ids in range(file_num):
            dst_id_count[ids] += [0] * \
                (self.nNeuron_per_tile * file_num - self.neuron_num)
            dst_id_cumsum = np.cumsum(
                [self.weight_addr_0] + dst_id_count[ids][:-1])  # 权重矩阵的地址要动态变化
            results.append((dst_id_cumsum << fanout).astype(
                "<u4") + np.array(dst_id_count[ids]).astype("<u4"))

        return results

    def weight_addr_int(self):
        if self.cfg == 3:
            # int8模式下8个神经元共享共用一个addr: 0-7, 8-15, ...
            group_size = 8
        elif self.cfg == 2:
            # int16模式下4个神经元共享共用一个addr: 0-3, 4-7, ...
            group_size = 4
        else:
            logger.error(
                f'Config.yaml cfg mode is {self.cfg}, not INT8/16 mode.')
        fanout = self.fanout
        dst_id_count = []
        results = []
        file_num = self.nTile_layout
        dst_id_count = [[] for _ in range(file_num)]
        tmp_list = [[] for _ in range(file_num)]
        for src_id, dst_ids in enumerate(self.connection_matrix.values()):
            for key in dst_ids.keys():
                tmp_list[int(key) // self.nNeuron_per_tile] += [key]
            if src_id % group_size == (group_size-1) or src_id + 1 == self.neuron_num:
                for i in range(file_num):
                    tmp_list[i] = list(set(tmp_list[i]))
                    dst_id_count[i].append(len(tmp_list[i]))
                tmp_list = [[] for _ in range(file_num)]

        for ids in range(file_num):
            dst_id_count[ids] += [0] * \
                (self.nNeuron_per_tile * file_num - self.neuron_num)
            dst_id_cumsum = np.cumsum(
                [self.weight_addr_0] + dst_id_count[ids][:-1])
            results.append((dst_id_cumsum << fanout).astype(
                "<u4") + np.array(dst_id_count[ids]).astype("<u4"))

        return results

    def default_init_value(self):
        # pylint: disable-next=too-many-function-args
        u_init_value = 0

        file_num = self.nTile_layout
        result = [[] for i in range(file_num)]
        for ids in range(file_num-1):
            idx_head = ids * 16384
            V_init = np.single(
                self.V_init[idx_head:idx_head+16384]).view("uint32").astype("<u4").tolist()
            result[ids] = [
                V_init +
                [0] * (16384 - self.nNeuron_per_tile),  # 3
                [10] * self.nNeuron_per_tile + [0] *
                (16384 - self.nNeuron_per_tile),  # 2
                [1] * self.nNeuron_per_tile + [0] *
                (16384 - self.nNeuron_per_tile),  # 1
                [0] * 16384,  # 0
                [0] * 16384,  # 7
                [u_init_value] * self.nNeuron_per_tile +
                [0] * (16384 - self.nNeuron_per_tile),  # 6
                [0] * 16384,  # 5
                [0] * 16384]  # 4
        # check V_init len
        if self.neuron_num - (file_num-1) * self.nNeuron_per_tile != len(self.V_init[idx_head+16384:]):
            logger.warning(
                f'last tile len(V_init) is {len(self.V_init[idx_head+16384:])}, need {self.neuron_num - (file_num-1) * self.nNeuron_per_tile}.')
            exit(1)
        V_init = np.single(
            self.V_init[idx_head+16384:]).view("uint32").astype("<u4").tolist()
        result[-1] = [
            V_init +
            [0] * (
                16384 - self.neuron_num + (file_num-1) * self.nNeuron_per_tile),
            [10] * (self.neuron_num - (file_num-1) * self.nNeuron_per_tile) + [0] * (
                16384 - self.neuron_num + (file_num-1) * self.nNeuron_per_tile),
            [1] * (self.neuron_num - (file_num-1) * self.nNeuron_per_tile) + [0] * (
                16384 - self.neuron_num + (file_num-1) * self.nNeuron_per_tile),
            [0] * 16384,
            [0] * 16384,
            [u_init_value] * (self.neuron_num - (file_num-1) * self.nNeuron_per_tile) + [0] * (
                16384 - self.neuron_num + (file_num-1) * self.nNeuron_per_tile),
            [0] * 16384,
            [0] * 16384,
        ]
        result = np.array(result).transpose(
            0, 2, 1).reshape(file_num, -1)

        return result

    def init_value_int(self):
        if self.cfg == 3:
            # int8模式下8个神经元共享共用一个addr: 0-7, 8-15, ...
            group_size = 8

            # 8个神经元共占256bit, 每个神经元4个8bit参数
            # (8bit)en = 1, t_last_sp = 10, v = 0, wacc = 0
            en_group = (1 << 24) + (1 << 16) + (1 << 8) + 1
            t_last_sp_group = (10 << 24) + (10 << 16) + (10 << 8) + 10
        elif self.cfg == 2:
            # int16模式下4个神经元共享共用一个addr: 0-3, 4-7, ...
            group_size = 4

            # 4个神经元共占256bit, 每个神经元4个16bit参数
            # (16bit)en = 1, t_last_sp = 10, v = 0, wacc = 0
            en_group = (1 << 16) + 1
            t_last_sp_group = (10 << 16) + 10
        else:
            logger.error(
                f'Config.yaml cfg mode is {self.cfg}, not INT8/16 mode.')

        # print(format(en_group, "032b"))
        # print(format(t_last_sp_group, "032b"))

        unit_num = self.neuron_num // group_size
        group_per_chip = self.nNeuron_per_tile // group_size

        file_num = self.nTile_layout
        result = [[] for _ in range(file_num)]
        for ids in range(file_num-1):
            result[ids] = [
                [0] * 16384,  # 3
                [0] * 16384,  # 2
                [t_last_sp_group] * group_per_chip + [0] *
                (16384 - group_per_chip),  # 1
                [en_group] * group_per_chip + [0] *
                (16384 - group_per_chip),  # 0
                [0] * 16384,  # 7
                [0] * 16384,  # 6
                [t_last_sp_group] * group_per_chip + [0] *
                (16384 - group_per_chip),  # 5
                [en_group] * group_per_chip + [0] *
                (16384 - group_per_chip)]  # 4
        last_file_neuron_num = unit_num - \
            (file_num-1) * group_per_chip
        result[-1] = [
            [0] * 16384,  # 3
            [0] * 16384,  # 2
            [t_last_sp_group] * last_file_neuron_num + [0] *
            (16384 - last_file_neuron_num),  # 1
            [en_group] * last_file_neuron_num + [0] *
            (16384 - last_file_neuron_num),  # 0
            [0] * 16384,  # 7
            [0] * 16384,  # 6
            [t_last_sp_group] * last_file_neuron_num + [0] *
            (16384 - last_file_neuron_num),  # 5
            [en_group] * last_file_neuron_num + [0] *
            (16384 - last_file_neuron_num)]  # 4
        result = np.array(result).transpose(
            0, 2, 1).reshape(file_num, -1)
        # print(result[0, :8])

        return result

    _initial_value: Optional[np.ndarray] = None
    """Initial value of each neuron. If not set, `self.default_init_value` will be used.
    """

    @ property
    def init_value(self) -> np.ndarray:
        """Initial value of each neuron.

        Returns:
            np.ndarray: Initial value of each neuron.
        """
        if self._initial_value is None:
            return self.default_init_value
        return self._initial_value

    @ init_value.setter
    def init_value(self, value: np.ndarray) -> None:
        """Set initial value of each neuron.

        Args:
            value (np.ndarray): Initial value.
        """
        self._initial_value = value

    def dst_weight(self):
        file_num = self.nTile_layout
        ex_neuron_num = int(self.neuron_num * self.neuron_scale)
        dst_and_weight = [[] for _ in range(file_num)]
        for src_id in range(ex_neuron_num):
            # content of line: [dst_id, weight value, dst_id, weight_value ...]
            # 突触存储的数据类型为：flag， neuron_id, weight_value_1， weight_value_2;在单个突触电流的情况下，flag不起作用，此时默认weight_value_2为0.
            for dst_id, weight_value in self.connection_matrix[src_id].items():
                # 兴奋性神经元的突触权重格式为：flag， neuron_id, weight_value，0
                chip_id = int(dst_id) // self.nNeuron_per_tile
                dst_id_tmp = dst_id - self.nNeuron_per_tile*chip_id
                w = np.single(weight_value).view("uint32")
                dst_and_weight[chip_id] += [0, w, dst_id_tmp, 0]

        for src_id in range(ex_neuron_num, self.neuron_num):
            for dst_id, weight_value in self.connection_matrix[src_id].items():
                # 抑制性神经元的突触权重格式为：flag， neuron_id, 0， weight_value
                chip_id = int(dst_id) // self.nNeuron_per_tile
                dst_id_tmp = dst_id - self.nNeuron_per_tile * chip_id
                w = np.single(weight_value).view("uint32")
                dst_and_weight[chip_id] += [w, 0, dst_id_tmp, 0]

        for i in range(file_num):
            dst_and_weight[i] = np.array([dst_and_weight[i]])

        return dst_and_weight

    def dst_weight_int(self):
        if self.cfg == 3:
            # int8模式下8个神经元共享共用一个addr: 0-7, 8-15, ...
            group_size = 8
        elif self.cfg == 2:
            # int16模式下4个神经元共享共用一个addr: 0-3, 4-7, ...
            group_size = 4
        else:
            logger.error(
                f'Config.yaml cfg mode is {self.cfg}, not INT8/16 mode.')

        # int8模式下只支持一种神经元类型, 8个src_id为一组
        file_num = self.nTile_layout
        neuron_num = self.neuron_num
        dst_and_weight = [[] for _ in range(file_num)]
        tmp_conn_mat = defaultdict(dict)
        for src_id in range(neuron_num):
            tmp_src_id = src_id % group_size
            for dst_id, weight_value in self.connection_matrix[src_id].items():
                tmp_conn_mat[dst_id][tmp_src_id] = weight_value

            if tmp_src_id + 1 == group_size or src_id + 1 == neuron_num:
                # 积累8个之后开始生成数据, 数据每32bit一个
                for dst_id in tmp_conn_mat.keys():
                    w = [0] * group_size
                    for src_id, weight_value in tmp_conn_mat[dst_id].items():
                        w[src_id] = np.int8(weight_value).view("uint8")

                    if self.cfg == 3:
                        # 拼接w1对应神经元0-3; w2对应神经元4-7
                        w1 = (w[3] << 24) + (w[2] << 16) + (w[1] << 8) + w[0]
                        w2 = (w[7] << 24) + (w[6] << 16) + (w[5] << 8) + w[4]
                    elif self.cfg == 2:
                        # 拼接w1对应神经元0-1; w2对应神经元2-3
                        w1 = (w[1] << 16) + w[0]
                        w2 = (w[3] << 16) + w[2]
                    else:
                        logger.error(
                            f'Config.yaml cfg mode is {self.cfg}, not INT8/16 mode.')

                    chip_id = int(dst_id) // self.nNeuron_per_tile
                    dst_id_tmp = dst_id - self.nNeuron_per_tile*chip_id
                    dst_and_weight[chip_id] += [w1, w2, dst_id_tmp, 0]

                # 每group_size个src生成后进行重置
                tmp_conn_mat = defaultdict(dict)

        for i in range(file_num):
            dst_and_weight[i] = np.array([dst_and_weight[i]])

        return dst_and_weight

    def write_to_bin(self, output_dir):
        output_dir = Path(output_dir) / 'weight'
        output_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
        file_num = self.nTile_layout
        print(f'used_tile: {file_num}')

        if self.cfg == 3 or self.cfg == 2:
            # part 1: 神经元索引
            weight_addr = self.weight_addr_int()

            # part 2: 神经元状态备份，每个神经元8个32bit
            init_value = self.init_value_int()

            # part 3: 连接+权重，每条128bit
            dst_weight = self.dst_weight_int()
        else:
            # part 1: 神经元索引
            weight_addr = self.weight_addr()

            # part 2: 神经元状态备份，每个神经元8个32bit
            init_value = self.init_value()

            # part 3: 连接+权重，每条128bit
            dst_weight = self.dst_weight()

        for ids in range(file_num):
            file_path = output_dir / f"weight_{ids}.bin"
            file_path.unlink(missing_ok=True)
            # index
            if os.path.exists(file_path):
                os.remove(file_path)

            file_path.unlink(missing_ok=True)
            Fake.fwrite(file_path=file_path,
                        arr=weight_addr[ids], dtype="<u4")
            Fake.fwrite(file_path=file_path,
                        arr=init_value[ids], dtype="<u4")
            Fake.fwrite(file_path=file_path,
                        arr=dst_weight[ids], dtype="<u4")
