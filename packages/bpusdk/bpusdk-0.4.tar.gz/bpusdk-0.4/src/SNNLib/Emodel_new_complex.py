import brainpy as bp
import numpy as np
from brainpy.synapses import Exponential
from typing import Callable
from functools import partial
import brainpy.math as bm
from brainpy._src.dyn.neurons import lif
from brainpy._src.initialize import (ZeroInit,
                                     OneInit,
                                     Constant,
                                     Initializer,
                                     parameter,
                                     variable_,
                                     noise as init_noise)
from brainpy._src.context import share
from jax.lax import stop_gradient
from brainpy._src.integrators import odeint, sdeint, JointEq
from typing import Union, Callable, Optional, Any, Sequence

from jax.lax import stop_gradient

import brainpy.math as bm
from brainpy._src.context import share
from brainpy._src.dyn.neurons import lif
import brainpy.math as bm
from brainpy.types import ArrayType
from typing import Union, Dict, Callable, Optional
from brainpy._src.dynsys import DynamicalSystem
import jax 
import random 
import warnings
from brainpy import math as bm
from brainpy._src.context import share
from brainpy._src.dyn.base import SynDyn
from brainpy._src.integrators.ode.generic import odeint
from brainpy._src.mixin import AlignPost, ReturnInfo
from brainpy.types import ArrayType
from BrainpyLib.BrainpyBase import BrainpyBase

from brainpy import math as bm, check
from brainpy._src.delay import (delay_identifier,
                                register_delay_by_return)
from brainpy._src.dynsys import DynamicalSystem, Projection
from brainpy._src.mixin import (JointType, ParamDescriber, SupportAutoDelay, BindCondData, AlignPost)

import brainpy.math as bm
from brainpy._src.context import share
from brainpy._src.dyn._docs import ref_doc, lif_doc, pneu_doc, dpneu_doc, ltc_doc, if_doc
from brainpy._src.dyn.neurons.base import GradNeuDyn
from brainpy._src.initialize import ZeroInit, OneInit, noise as init_noise
from brainpy._src.integrators import odeint, sdeint, JointEq
from brainpy.check import is_initializer
from brainpy.types import Shape, ArrayType, Sharding
from pathlib import Path
import pickle

warnings.filterwarnings('ignore')

class myFullProjAlignPost(Projection):
  def __init__(
      self,
      pre: JointType[DynamicalSystem, SupportAutoDelay],
      delay: Union[None, int, float],
      comm: DynamicalSystem,
      syn: JointType[DynamicalSystem, AlignPost],
      out: JointType[DynamicalSystem, BindCondData],
      post: DynamicalSystem,
      out_label: Optional[str] = None,
      name: Optional[str] = None,
      mode: Optional[bm.Mode] = None,
  ):
    super().__init__(name=name, mode=mode)

    # synaptic models
    check.is_instance(pre, JointType[DynamicalSystem, SupportAutoDelay])
    check.is_instance(comm, DynamicalSystem)
    check.is_instance(syn, JointType[DynamicalSystem, AlignPost])
    check.is_instance(out, JointType[DynamicalSystem, BindCondData])
    check.is_instance(post, DynamicalSystem)
    self.comm = comm
    self.syn = syn

    # delay initialization
    delay_cls = register_delay_by_return(pre)
    delay_cls.register_entry(self.name, delay)

    # synapse and output initialization
    post.add_inp_fun(self.name, out, label=out_label)

    # references
    self.refs = dict()
    # invisible to ``self.nodes()``
    self.refs['pre'] = pre
    self.refs['post'] = post
    self.refs['out'] = out
    # unify the access
    self.refs['delay'] = delay_cls
    self.refs['comm'] = comm
    self.refs['syn'] = syn

  def update(self):
    x = self.refs['delay'].at(self.name)
    g = self.syn(self.comm(x))
    self.refs['out'].bind_cond(g)  # synapse post current
    return g

  delay = property(lambda self: self.refs['delay'])
  pre = property(lambda self: self.refs['pre'])
  post = property(lambda self: self.refs['post'])
  out = property(lambda self: self.refs['out'])


# eqvivalent with VV - (exp(-TT/tau) - 1)*(V_rest - VV + XX): XX, VV, TT = a, b, c
def lif_generated_function_dt1(shape, V_rest, tau, XX, VV, TT):
    dt = bm.get_dt()
    dV =  (V_rest-VV+XX)/tau
    Vnew = VV + dV* dt
    return Vnew

# eqvivalent with TT*exp(-GG/tau): GG,TT = a,b
def syn_generated_function_dt1(shape,tau,GG, TT):
    dt = bm.get_dt()
    dG = -GG/tau
    GG = GG + dG*dt
    return GG

#eqvivalent to bp.dyn.LifRef
class my_LifRef(lif.LifRefLTC):
  def derivative(self, V, t, I):
    return (-V + self.V_rest + self.R * I) / self.tau

  def update(self, x=None):
    #self.integral = odeint(method=method, f=self.derivative,show_code=True)

    #------------LifRef(LifRefLTC)------------
    x = 0. if x is None else x
    x = self.sum_current_inputs(self.V.value, init=x)
    #return super().update(x)

    #-----------LifRefLTC(LifLTC)-----------
    t = share.load('t')
    dt = share.load('dt')
    x = 0. if x is None else x

    # integrate membrane potential
  
    V = self.integral(self.V.value, t, x, dt) + self.sum_delta_inputs()
    #V =  lif_generated_function_dt1(self.size, self.V_rest,self.tau, x, self.V.value, jax.numpy.ones(self.size, jax.numpy.float32)*dt) + self.sum_delta_inputs()
    #V = lif_generated_function_ori(self.size, x, self.V.value, jax.numpy.ones(self.size, jax.numpy.float32)*dt) + self.sum_delta_inputs()
    
    
    #V = self.V.value - (np.exp(-1/self.tau) - 1)*(self.V_rest - self.V.value + x) + self.sum_delta_inputs()
    
    # refractory
    refractory = (t - self.t_last_spike) <= self.tau_ref
    # if isinstance(self.mode, bm.TrainingMode):
    #   refractory = stop_gradient(refractory)
    V = bm.where(refractory, self.V.value, V)

    # spike, refractory, spiking time, and membrane potential reset
    # if isinstance(self.mode, bm.TrainingMode):
    #   spike = self.spk_fun(V - self.V_th)
    #   spike_no_grad = stop_gradient(spike) if self.detach_spk else spike
    #   if self.spk_reset == 'soft':
    #     V -= (self.V_th - self.V_reset) * spike_no_grad
    #   elif self.spk_reset == 'hard':
    #     V += (self.V_reset - V) * spike_no_grad
    #   else:
    #     raise ValueError
    #   spike_ = spike_no_grad > 0.
    #   # will be used in other place, like Delta Synapse, so stop its gradient
    #   if self.ref_var:
    #     self.refractory.value = stop_gradient(bm.logical_or(refractory, spike_).value)
    #   t_last_spike = stop_gradient(bm.where(spike_, t, self.t_last_spike.value))

    # else:
    spike = V > self.V_th
    V = bm.where(spike, self.V_reset, V)
    # if self.ref_var:
    #   self.refractory.value = bm.logical_or(refractory, spike)
    t_last_spike = bm.where(spike, t, self.t_last_spike.value)

    self.V.value = V
    self.spike.value = spike
    self.t_last_spike.value = t_last_spike
    return spike

#eqvivalant with bp.dyn.Expon
class my_Expon(SynDyn, AlignPost):
  def __init__(
      self,
      size: Union[int, Sequence[int]],
      keep_size: bool = False,
      sharding: Optional[Sequence[str]] = None,
      method: str = 'exp_auto',
      name: Optional[str] = None,
      mode: Optional[bm.Mode] = None,

      # synapse parameters
      tau: Union[float, ArrayType, Callable] = 8.0,
  ):
    super().__init__(name=name,
                     mode=mode,
                     size=size,
                     keep_size=keep_size,
                     sharding=sharding)

    # parameters
    self.tau = self.init_param(tau)

    # functionodeint
    self.integral = odeint(self.derivative, method=method,show_code=True)
    self._current = None

    self.reset_state(self.mode)

  def derivative(self, g, t):
    return -g / self.tau

  def reset_state(self, batch_or_mode=None, **kwargs):
    self.g = self.init_variable(bm.zeros, batch_or_mode)

  def update(self, x=None):
    #self.integral.showcode = True
    self.g.value = self.integral(self.g.value, share['t'], share['dt'])
    #self.g.value = syn_generated_function_dt1(self.size, self.tau, self.g.value, jax.numpy.ones(self.size, jax.numpy.float32)*share.load('dt'))
    
    #self.g.value = syn_generated_function_ori(self.size, jax.numpy.ones(self.size, jax.numpy.float32)*share.load('dt'),self.g.value)
    
    #self.g.value = np.exp(-1/self.tau) * self.g.value 

    if x is not None:
      self.add_current(x)
    return self.g.value

  def add_current(self, x):
    self.g.value += x

  def return_info(self):
    return self.g

    
class Exponential(bp.Projection): 
  def __init__(self, pre, post, delay, prob, g_max, tau, E, method,allow_multi_conn):
    super().__init__()
    self.pron = myFullProjAlignPost(
      pre=pre,
      delay=delay,
      # Event-driven computation
      comm=bp.dnn.EventCSRLinear(bp.conn.FixedProb(prob, pre=pre.num, post=post.num,seed = 42, allow_multi_conn=allow_multi_conn), g_max), 
      syn=my_Expon(size=post.num, tau=tau,method=method),# Exponential synapse
      out=bp.dyn.COBA(E=E), # COBA network
      post=post
    )

  def update(self, *args, **kwargs):
    nodes = tuple(self.nodes(level=1, include_self=False).subset(DynamicalSystem).unique().values())
    if len(nodes):
      for node in nodes:
        node.update(*args, **kwargs)
    else:
      raise ValueError('Do not implement the update() function.')
 

class EINet(bp.DynamicalSystem):
    def __init__(self, ne, ni, connect_prob, method, allow_multi_conn):
        super().__init__()
        self.neuron_scale = 1
        tauRef = bm.get_dt()*5.+0.0001 # Make sure tauRef always == 5 timesteps 
        self.E = my_LifRef(ne, V_rest=1., V_th=10., V_reset=1., tau=1., tau_ref=tauRef,
                               V_initializer=Constant(1.),method=method)


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
    bm.set_dt(2.)
    total_time = 100  # ms
    nStep = int(total_time / bm.get_dt())
    inpE = 1.

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
