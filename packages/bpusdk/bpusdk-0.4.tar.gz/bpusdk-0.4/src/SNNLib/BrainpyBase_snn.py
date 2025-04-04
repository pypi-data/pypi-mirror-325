import copy
import math
import pickle
import re
from collections import defaultdict

import brainpy as bp
import brainpy.math as bm
import numpy as np
from addict import Dict as AttrDict
from brainpy._src.dyn.neurons.base import GradNeuDyn, NeuDyn
from brainpy._src.initialize import parameter, variable_
from scipy.sparse import csr_matrix
from brainpy._src.context import share

# Return true if Proj is valid
def checkAttr(proj):
    cond1 = hasattr(proj, "comm") and hasattr(
        proj, "syn") and hasattr(proj, "pre") and hasattr(proj, "post")
    if hasattr(proj, "refs"):
        cond2 = ("comm" in proj.refs) and ("syn" in proj.refs) and (
            "pre" in proj.refs) and ("post" in proj.refs)
        return cond1 or cond2
    return cond1

# Subtract value from FullPeojAlign or exponential


def getAttribute(element, attribute):
    if hasattr(element, "refs"):
        return element.refs[attribute]
    else:
        if attribute == "out":
            attribute = "output"
        return getattr(element, attribute)


class BrainpyBase():
    def __init__(self, network, inpE, seed=42) -> None:
        self.network = network
        self.seed = seed

        self.cv = AttrDict()
        self.count_neuron()
        self.count_proj()

        self.get_neuron_property()
        self.get_proj_property()

        self.cv["I_input"] = inpE

        # v_parameter_dict = {"LIFref":["V_reset","V_th","tau_ref","V_rest","tau","R"]}
        # v_func_dict = {"LIFref": {"V": lambda I, V: V - self.cv["tauExp"]*(self.cv["V_rest"-V+I])}}

    #  self.index_map = {}
    #  self.neuron_name_dict = {}

    def count_neuron(self):
        # Substract nNeuron and index for each population
        self.index_map = {}
        self.neuron_name_dict = {}
        last_index = 0
        for iNeuron_group, neuron_group in enumerate(self.network.nodes().subset(NeuDyn).values()):
            start_index = last_index
            #end_index = start_index + neuron_group.size[0]
            end_index = (iNeuron_group+1)*(16*1024)            
            self.index_map[neuron_group.name] = (start_index, end_index)
            last_index = end_index

            name = ''.join(re.findall(r'[a-zA-Z]', neuron_group.name))
            if name not in self.neuron_name_dict.keys():
                self.neuron_name_dict[name] = 1
            else:
                self.neuron_name_dict[name] += 1

        for iNeuron_group_fake in range(iNeuron_group,5):
            start_index = last_index
            end_index = start_index+(16*1024)   
            name = f"fake_{iNeuron_group_fake+1}"          
            self.index_map[name] = (start_index, end_index)
            last_index = end_index

            name = ''.join(re.findall(r'[a-zA-Z]', name))
            if name not in self.neuron_name_dict.keys():
                self.neuron_name_dict[name] = 1
            else:
                self.neuron_name_dict[name] += 1 
        print(1)

    #  self.synapse_dict = {}
    #  self.syn_name_dict = {}
    #  self.out_name_dict = {}
    def count_proj(self):
      # Sort synapse by pre in dict and extract syn/out name & number
        self.synapse_dict = {}
        self.syn_name_dict = {}
        self.out_name_dict = {}
        for proj in self.network.nodes().subset(bp.Projection).values():
            if checkAttr(proj):
                pre = getAttribute(proj, "pre")
                if pre in self.synapse_dict:
                    self.synapse_dict[pre].append(proj)
                else:
                    self.synapse_dict[pre] = [proj]

                out_name = getAttribute(proj, "out").name
                out_name = ''.join(re.findall(r'[a-zA-Z]', out_name))
                if out_name not in self.out_name_dict.keys():
                    self.out_name_dict[out_name] = 1
                else:
                    self.out_name_dict[out_name] += 1

                syn_name = getAttribute(proj, "syn").name
                syn_name = ''.join(re.findall(r'[a-zA-Z]', syn_name))
                if syn_name not in self.syn_name_dict.keys():
                    self.syn_name_dict[syn_name] = 1
                else:
                    self.syn_name_dict[syn_name] += 1

    def get_neuron_property(self):
        # Assume E and I have identical parameters & V_reset、V_th、tau_ref exist
        # TODO: supprt other neuron type
        self.Vinit = np.zeros(self.get_neuron_num())
        count = 0
        bm.random.seed(self.seed)
        for neuronGroup in self.network.nodes().subset(NeuDyn).values():
            self.neuronName = neuronGroup.name
            self.cv["V_reset"] = getattr(neuronGroup, "V_reset")
            self.cv["V_th"] = getattr(
                neuronGroup, "V_th", -50.) 
            self.cv["tau_ref"] = 0.
            self.cv["V_rest"] = getattr(neuronGroup, "V_rest")
            self.cv["tau"] = getattr(neuronGroup, "tau")
            self.cv["R"] = getattr(neuronGroup, "R")
            self.cv["dt"] = bm.get_dt()

            # self.scaling.offset_scaling(variable_(copy.deepcopy(neuronGroup._V_initializer), sizes=neuronGroup.size), bias=None, scale=None)
            Vinit_local = variable_(neuronGroup._V_initializer,
                               sizes=neuronGroup.size).value
            self.Vinit[count*16*1024:count*16*1024+neuronGroup.size[0]]=(Vinit_local)
        #print(1)

    def get_proj_property(self):
        # Extract tau and E for first synapse for each pre
        for iPre, pre in enumerate(self.synapse_dict):
            proj = self.synapse_dict[pre][0]
            self.cv[f"tau{iPre}"] = proj.syn.tau
            self.synapseName = ''.join(re.findall(
                r'[a-zA-Z]', getAttribute(proj, "out").name))
            if self.synapseName == 'COBA':
                self.cv[f"E{iPre}"] = getAttribute(proj, "out").E if hasattr(
                    proj, "refs") else proj.output.E

    def get_connection_matrix(self):
        # Substract connection layers
        self.layers = {}
        for name in self.network.nodes().subset(bp.Projection):
            if re.match(r"[A-Z]\w+\d+", name) and checkAttr(self.network.nodes().subset(bp.Projection)[name]):
                self.layers[name] = self.network.nodes().subset(bp.Projection)[
                    name]

        self.connection_matrix = defaultdict(dict)
        for conn in self.layers.values():
            src_offset = self.index_map[getAttribute(conn, "pre").name][0]
            dst_offset = self.index_map[getAttribute(conn, "post").name][0]

            if isinstance(conn.comm, bp.dnn.EventCSRLinear):
                indices = conn.comm.indices
                indptr = conn.comm.indptr
                rows = indptr.size - 1
                cols = int(np.max(indices) + 1)
                if isinstance(conn.comm.weight, float):
                    data = np.ones(indptr[-1]) * conn.comm.weight
                    compressed = csr_matrix((data, indices, indptr), shape=(
                        rows, cols), dtype=np.float32).tocoo()
                    for i, j, k in zip(compressed.row, compressed.col, compressed.data):
                        src_abs_id = int(i + src_offset)
                        dst_abs_id = int(j + dst_offset)
                        self.connection_matrix[src_abs_id][dst_abs_id] = k
                else:
                    data = np.ones(
                        indptr[-1], dtype=np.uint32) * conn.comm.weight
                    compressed = csr_matrix((data, indices, indptr), shape=(
                        rows, cols), dtype=np.uint32).tocoo()
                    for i, j, k in zip(compressed.row, compressed.col, compressed.data):
                        src_abs_id = int(i + src_offset)
                        dst_abs_id = int(j + dst_offset)
                        self.connection_matrix[src_abs_id][dst_abs_id] = k

            elif isinstance(conn.comm, bp.dnn.EventJitFPHomoLinear):
                conn_matrix = conn.comm.get_conn_matrix()
                compressed = csr_matrix(
                    conn_matrix, dtype=np.float32).tocoo()
                if isinstance(conn.comm.weight, float):
                    data = np.ones(compressed.row.size) * conn.comm.weight
                    for i, j, k in zip(compressed.col, compressed.row, compressed.data):
                        src_abs_id = int(i + src_offset)
                        dst_abs_id = int(j + dst_offset)
                        self.connection_matrix[src_abs_id][dst_abs_id] = np.single(
                            k).view("uint32")
                else:
                    data = np.ones(compressed.row.size,
                                   dtype=np.uint32) * conn.comm.weight
                    for i, j, k in zip(compressed.col, compressed.row, compressed.data):
                        src_abs_id = int(i + src_offset)
                        dst_abs_id = int(j + dst_offset)
                        self.connection_matrix[src_abs_id][dst_abs_id] = np.uint32(
                            k).view("uint32")
            
            elif isinstance(conn.comm, bp.dnn.Dense):
                compressed = csr_matrix(conn.comm.W, dtype=np.float32).tocoo()
                for i, j, k in zip(compressed.row, compressed.col, compressed.data):
                    src_abs_id = int(i + src_offset)
                    dst_abs_id = int(j + dst_offset)
                    self.connection_matrix[src_abs_id][dst_abs_id] = k
            else:
                raise NotImplementedError

        # with open('filename.pickle', 'wb') as handle:
        #     pickle.dump(self.connection_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return self.connection_matrix

    def get_neuron_num(self):
        # 返回每一层的神经元的指数范围
        """Neuron layer to neuron start index and end index. e.g.

        ```python
        {"X": (0, 784), "Y": (784, 1409)}
        ```

        or

        ```python
        {"LIF0": (0, 3200), "LIF1": (3200, 4000)}
        ```

        In this example, the total number of neurons is 1409.
        layer with name "X" has 784 neurons and the index of them starts with 0.
        layer with name "Y" has 625 neurons (1409-625). Starts from 784 and ends at 1409 (exclusive).
        The index is 0-based indexing.
        """

        self.neuron_num = max(
            end_index for _, end_index in self.index_map.values())
        return self.neuron_num

    @property
    def neuron_nums(self):
        """获得neuron_num的数量

        Returns:
            int: 模型中neuron_num的总数
        """
        return self.neuron_num

    @property
    def v_func(self,):
        """从模型中解析膜电位更新公式

        Returns:
            funcs: 膜电位更新公式
        """
        return {"V": lambda I, V: V + (self.cv["V_rest"]-V+self.cv["R"]*(I+self.cv["I_input"]))/self.cv["tau"]*self.cv["dt"]}
    
    @property
    # out
    def i_func(self,):
        """定义膜电位更新公式中的I

        Returns:
            funcs: 膜电位更新公式中的I
        """
        return {
            "I": lambda g1, g2: g1 + g2 ,
        }
    
        # return {
        #     "I": lambda g0, g1, V: self.cv['R'] * g0 * (self.cv['E0'] - V) + 
        #                             self.cv['R'] * g1 * (self.cv['E1'] - V),
        # }
        

    @property
    # syn
    def g_func(self,):
        """定义突触模型中的电导g

        Returns:
            funcs: 突触模型中的电导g
        """
        return {
            "g1": lambda g1: g1 - g1/self.cv['tau0']*self.cv['dt'],
            "g2": lambda g2: g2 - g2/self.cv['tau1']*self.cv['dt'],
        }

    @property
    def v_variables(self,):
        """从模型中解析膜电位更新公式中的所有变量

        Returns:
            list: 膜电位所有变量
        """
        for ds in self.network.nodes().subset(NeuDyn).values():
            return ds.integral.variables

    @property
    def remaining_params(self,):
        """从模型中解析膜电位更新公式中除了V, I之外的其它参数

        Returns:
            list: 膜电位更新公式中除了V, I之外的其它参数
        """
        return [key for key in self.v_variables if key not in ('V', 't', 'I')]  # "R6" ~ "R7"
