import random
import warnings
from pathlib import Path

import brainpy as bp
import jax
import numpy as np
from brainpy import math as bm
from brainpy._src.dynsys import DynamicalSystem
from brainpy._src.initialize import Constant, OneInit, ZeroInit
from brainpy._src.initialize import noise as init_noise
import pickle
from BrainpyLib.BrainpyBase import BrainpyBase
#from BrainpyBase import BrainpyBase
from brainpy._src.initialize.base import _InterLayerInitializer
from brainpy import math as bm, tools

warnings.filterwarnings('ignore')


def createConn(nNeuron,fanOut,groupSize):
    iNeuron_list = list(np.arange(nNeuron))
    nGroup = int(np.ceil(nNeuron/groupSize)) #last group may have a different size
    group_pre_list = list(np.arange(nGroup))
    group_pre_list = [item for item in group_pre_list for _ in range(fanOut)]
    if fanOut < groupSize:
        # with no replacement -> act as pre once/never
        # risk for self connection
        group_post_list = random.sample(iNeuron_list, k=len(group_pre_list))
    else:
        group_post_list = random.choice(iNeuron_list, k=len(group_pre_list))
        #TODO: check multiple connection here
    pre_list = []
    post_list = []
    for pre,post in zip(group_pre_list,group_post_list):
        if pre == nGroup:
            tmp_pre = np.arange(pre*groupSize,nNeuron)
            tmp_post = [post]*len(tmp_pre)
        else:
            tmp_pre = np.arange(pre*groupSize,pre*groupSize+groupSize)
            tmp_post = [post]*groupSize
        pre_list.extend(tmp_pre)
        post_list.extend(tmp_post)
    # np.save("pre_list",pre_list)
    # np.save("post_list",post_list)
    return pre_list,post_list

def createInitV(nNeuron,fanOut,groupSize):
    np.zeros(())

class Customized_initializer(_InterLayerInitializer):
  """Constant initializer.

  Initialize the weights with the given values.

  Parameters
  ----------
  value : float, int, bm.ndarray
    The value to specify.
  """

  def __init__(self, value=1.):
    super(Customized_initializer, self).__init__()
    self.value = value

  def __call__(self, shape, dtype=None):
    shape = [tools.size2num(d) for d in shape]
    return bm.ones(shape, dtype=dtype) * self.value

  def __repr__(self):
    return f'{self.__class__.__name__}(value={self.value})'
  
class Exponential(bp.Projection):
    def __init__(self, pre, post, delay, prob, g_max, tau, E, method, allow_multi_conn):
        super().__init__()
        self.pron = bp.dyn.FullProjAlignPost(
            pre=pre,
            delay=delay,
            # comm=bp.dnn.EventJitFPHomoLinear(pre.num, post.num,prob=prob, weight=g_max, seed = 42),
            comm=bp.dnn.EventCSRLinear(bp.conn.FixedProb(prob, pre=pre.num, post=post.num, seed=42, allow_multi_conn=allow_multi_conn), g_max),
            syn=bp.dyn.Expon(size=post.num, tau=tau,method=method),  # Exponential synapse
            out=bp.dyn.COBA(E=E),  # COBA network
            post=post
        )


class EINet(bp.DynamicalSystem):
    def __init__(self, ne, ni, connect_prob, method, allow_multi_conn):
        super().__init__()
        self.neuron_scale = 1
        tauRef = bm.get_dt()*5.+0.0001 # Make sure tauRef always == 5 timesteps 
        self.E = bp.dyn.LifRef(ne, V_rest=0., V_th=10., V_reset=0., tau=1., tau_ref=tauRef,
                               V_initializer=Constant(3.),method=method)


        self.E2E = Exponential(self.E, self.E, delay=0.,
                               prob=connect_prob, g_max=1, tau=1., E=0.,method=method,allow_multi_conn=allow_multi_conn)

    def update(self, inpE):
        self.E2E()
        self.E(inpE)
        # monitor
        return self.E.spike

    def dump(self,download_path,inpE,nStep,jit=True): 
        runner = bp.DSRunner(
            self, monitors=['E.spike', 'E.V','E2E.pron.syn.g'], jit=jit)
        _ = runner.run(inputs=bm.ones(nStep) * inpE)
        E_sps = runner.mon['E.spike']
        E_V = runner.mon['E.V']
        E2E = runner.mon['E2E.pron.syn.g']

        download_path = f"{download_path}/soft_data"
        download_dir = Path(download_path)
        download_dir.mkdir(exist_ok=True,parents=True)
        np.save(download_dir / "N_V.npy", E_sps)
        np.save(download_dir / "N_spike.npy", E_V)
        np.save(download_dir / "N_wacc1.npy", E2E)

        
        test = BrainpyBase(self, 42)
        conn_matrix = test.get_connection_matrix()
        cv = test.cv
        with open(f'{download_dir}/connection.pickle', 'wb') as handle:
            pickle.dump(conn_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    random.seed(1)
    bm.random.seed(42)
    
    # Scope paramter
    scope = 96
    nNeuron = scope*1024
    nExc = int(nNeuron/2)
    nInh = int(nNeuron/2)
    nNeuron = nExc+nInh
    connect_prob = 5 / nNeuron
    net = EINet(nExc, nInh,connect_prob,method = "euler", allow_multi_conn= True)

    # Simulation parameter 
    bm.set_dt(1.)
    total_time = 100  # ms
    nStep = int(total_time / bm.get_dt())
    inpE = 5.

    # bp.integrators.compile_integrators(net.step_run, 0, 0.)
    # for intg in net.nodes().subset(bp.Integrator).values():
    #   print(intg.to_math_expr())

    # Alt1 
    runner = bp.DSRunner(
        net, monitors=['E.spike', 'E.V','E2E.pron.syn.g'], jit=False)
    Is = bm.ones(nStep) * inpE
    _ = runner.run(inputs=Is)
    E_sps = runner.mon['E.spike']
    E_V = runner.mon['E.V']
    E2E = runner.mon['E2E.pron.syn.g']

    # s = np.concatenate((E_sps, I_sps), axis=1)
    # V = np.concatenate((E_V, I_V), axis=1)
    # wacc1 = np.concatenate((I2E, I2I), axis=1)
    # wacc2 = np.concatenate((E2E, E2I), axis=1)

    # download_dir = Path('./tmp96_new/soft_data')
    # download_dir.mkdir(exist_ok=True,parents=True)
    # np.save(download_dir / "N_V.npy", V)
    # np.save(download_dir / "N_spike.npy", s)
    # np.save(download_dir / "N_wacc1.npy", wacc1)
    # np.save(download_dir / "N_wacc2.npy", wacc2)

    
    test = BrainpyBase(net, inpE)
    conn_matrix = test.get_connection_matrix()
    cv = test.cv
    # with open('./tmp96_new/soft_data/connection.pickle', 'wb') as handle:
    #     pickle.dump(conn_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Alt 2
    # def run_fun(i):
    #   return net.step_run(i, inpE)
    # indices = np.arange(total_step)  # arange by step
    # E_sps, I_sps = bm.for_loop(run_fun, indices)
    # E_sps = E_sps.value
    # I_sps = I_sps.value

    # Print
    data = np.sum(E_sps, axis=1) 
    print(data)

    # Vis
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 4.5))
    total_time = 100
    nStep = int(100. / bm.get_dt())
    indices = np.arange(nStep)
    ts = indices * bm.get_dt()
    plt.subplot(121)
    bp.visualize.raster_plot(ts, E_sps, show=False)
    plt.savefig("tmp")
