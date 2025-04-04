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
#from .BrainpyBase import BrainpyBase
from BrainpyLib.BrainpyBase import BrainpyBase

warnings.filterwarnings('ignore')


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
        self.neuron_scale = 0.5
        self.E = bp.dyn.LifRef(ne, V_rest=-60., V_th=-50., V_reset=-60., tau=20., tau_ref=1.0,
                               V_initializer=bp.init.Normal(-55., 2.),method=method)
        self.I = bp.dyn.LifRef(ni, V_rest=-60., V_th=-50., V_reset=-60., tau=20., tau_ref=1.0,
                               V_initializer=bp.init.Normal(-55., 2.),method=method)
        # self.E = bp.dyn.LifRef(ne, V_rest=-60., V_th=-50., V_reset=-60., tau=20., tau_ref=5.,
        #                        V_initializer=bp.init.ZeroInit())
        # self.I = bp.dyn.LifRef(ni, V_rest=-60., V_th=-50., V_reset=-60., tau=20., tau_ref=5.,
        #                        V_initializer=bp.init.ZeroInit())

        self.E2E = Exponential(self.E, self.E, delay=0.,
                               prob=connect_prob, g_max=0.6, tau=5., E=0.,method=method,allow_multi_conn=allow_multi_conn)
        self.E2I = Exponential(self.E, self.I, delay=0.,
                               prob=connect_prob, g_max=0.6, tau=5., E=0.,method=method,allow_multi_conn=allow_multi_conn)
        self.I2E = Exponential(self.I, self.E, delay=0.,
                               prob=connect_prob, g_max=6.7, tau=10., E=-80.,method=method,allow_multi_conn=allow_multi_conn)
        self.I2I = Exponential(self.I, self.I, delay=0.,
                               prob=connect_prob, g_max=6.7, tau=10., E=-80.,method=method,allow_multi_conn=allow_multi_conn)

    def update(self, inpE):
        self.E2E()
        self.E2I()
        self.I2E()
        self.I2I()
        self.E(inpE)
        self.I(inpE)
        # monitor
        return self.E.spike, self.I.spike

    def dump(self,download_path,inpE,nStep,jit=True): 
        runner = bp.DSRunner(
            self, monitors=['E.spike', 'I.spike', 'E.V', 'I.V','E2E.pron.syn.g','E2I.pron.syn.g','I2E.pron.syn.g','I2I.pron.syn.g'], jit=True)
        _ = runner.run(inputs=bm.ones(nStep) * inpE)
        E_sps = runner.mon['E.spike']
        I_sps = runner.mon['I.spike']
        E_V = runner.mon['E.V']
        I_V = runner.mon['I.V']
        E2E = runner.mon['E2E.pron.syn.g']
        E2I = runner.mon['E2I.pron.syn.g']
        I2E = runner.mon['I2E.pron.syn.g']
        I2I = runner.mon['I2I.pron.syn.g']

        s = np.concatenate((E_sps, I_sps), axis=1)
        V = np.concatenate((E_V, I_V), axis=1)
        wacc1 = np.concatenate((I2E, I2I), axis=1)
        wacc2 = np.concatenate((E2E, E2I), axis=1)

        download_path = f"{download_path}/soft_data"
        download_dir = Path(download_path)
        download_dir.mkdir(exist_ok=True,parents=True)
        np.save(download_dir / "N_V.npy", V)
        np.save(download_dir / "N_spike.npy", s)
        np.save(download_dir / "N_wacc1.npy", wacc1)
        np.save(download_dir / "N_wacc2.npy", wacc2)
        
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
    nExc = 3200
    nInh = 800
    nNeuron = nExc+nInh
    connect_prob = 0.02
    net = EINet(nExc, nInh,connect_prob,method = "exp_auto", allow_multi_conn= True)

    # Simulation parameter 
    bm.set_dt(0.5)
    total_time = 100  # ms
    nStep = int(total_time / bm.get_dt())
    inpE = 20.

    # bp.integrators.compile_integrators(net.step_run, 0, 0.)
    # for intg in net.nodes().subset(bp.Integrator).values():
    #   print(intg.to_math_expr())

    # Alt1 
    runner = bp.DSRunner(
        net, monitors=['E.spike', 'I.spike', 'E.V', 'I.V','E2E.pron.syn.g','E2I.pron.syn.g','I2E.pron.syn.g','I2I.pron.syn.g'], jit=True)
    Is = bm.ones(nStep) * inpE
    _ = runner.run(inputs=Is)
    E_sps = runner.mon['E.spike']
    I_sps = runner.mon['I.spike']
    E_V = runner.mon['E.V']
    I_V = runner.mon['I.V']
    E2E = runner.mon['E2E.pron.syn.g']
    E2I = runner.mon['E2I.pron.syn.g']
    I2E = runner.mon['I2E.pron.syn.g']
    I2I = runner.mon['I2I.pron.syn.g']

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

    
    test = BrainpyBase(net, 42)
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
    data = np.sum(E_sps, axis=1) + np.sum(I_sps, axis=1)
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
    plt.subplot(122)
    bp.visualize.raster_plot(ts, I_sps, show=True)
    plt.savefig("tmp")
