import time
import brainpy as bp
import numpy as np
from brainpy.neurons import LIF
from brainpy.synapses import Exponential
import jax
import brainpy.math as bm
import matplotlib.pyplot as plt
import json 
import pickle
import warnings
import numpy as np
from matplotlib.gridspec import GridSpec
#from .BrainpyBase_snn import BrainpyBase
from BrainpyBase_snn import BrainpyBase
from pathlib import Path

class Exponential(bp.Projection): 
  def __init__(self, pre, post, tau):
    super().__init__()
    self.pron = bp.dyn.FullProjAlignPost(
      pre=pre,
      delay = 0,
      comm=bp.dnn.Linear(pre.num, post.num, W_initializer=bp.init.KaimingNormal(scale=20.), b_initializer=None), 
      syn=bp.dyn.Expon(size=post.num, tau=tau,method='euler'),
      out=bp.dyn.CUBA(), 
      post = post
      )

class Exponential_prob(bp.Projection):
    def __init__(self, pre, post, tau):
        super().__init__()
        self.pron = bp.dyn.FullProjAlignPost(
            pre=pre,
            delay=0.,
            comm=bp.dnn.EventCSRLinear(bp.conn.FixedProb(1., pre=pre.num, post=post.num, seed=42, allow_multi_conn=False), 0.01),
            syn=bp.dyn.Expon(size=post.num, tau=tau,method='euler'),  # Exponential synapse
            out=bp.dyn.CUBA(),  # COBA network
            post=post
        )

class SNN(bp.DynamicalSystem):
  def __init__(self, num_in, num_rec, num_out):
    super().__init__()
    self.neuron_scale = 1
    
    # parameters
    self.num_in = num_in
    self.num_rec = num_rec
    self.num_out = num_out

    # neuron groups
    self.i = bp.dyn.LifRef(num_in , tau=10., V_reset=0., V_rest=0., V_th=10., R=1.,spk_reset = 'hard',tau_ref=0.,method='euler')
    self.r = bp.dyn.LifRef(num_rec, tau=10., V_reset=0., V_rest=0., V_th=10., R=1.,spk_reset = 'hard',tau_ref=0.,method='euler')
    self.o = bp.dyn.LifRef(num_out, tau=10., V_reset=0., V_rest=0., V_th=10., R=1.,spk_reset = 'hard',tau_ref=0.,method='euler')

    self.i2r = Exponential(self.i, self.r, 10.)
    self.i2r.pron.comm.W = np.load("./i2r_W.npy")
    self.r2o = Exponential(self.r, self.o, 10.)
    self.r2o.pron.comm.W = np.load("./r2o_W.npy")

  def update(self, spike):
    # self.i2r.pron.refs['pre'].spike.value += spike
    # self.i2r()
    # self.r2o()

    # self.i()     
    # self.r() 
    # self.o() 

    self.i2r.pron.refs['pre'].spike.value += spike
    self.i2r()
    self.r() 
    self.r2o()
    self.o() 

    return self.o.V.value
    #return self.o.spike.value
    
  def dump(self, download_path,inpS,jit=True):
    runner = bp.DSRunner(self, data_first_axis='T', monitors=['i.spike', 'i.V', 'r.spike', 'r.V','o.spike','o.V','i2r.pron.syn.g','r2o.pron.syn.g'],jit=False)
    _ = runner.run(inputs=inpS.astype(bool))

    S = np.zeros((8,96*1024))
    S[:,0       : self.num_in]            = runner.mon['i.spike']
    S[:,16*1024 : (16*1024+self.num_rec)] = runner.mon['r.spike']
    S[:,32*1024 : (32*1024+self.num_out)] = runner.mon['o.spike']

    V = np.zeros((8,96*1024))
    V[:,0       : self.num_in]            = runner.mon['i.V']
    V[:,16*1024 : (16*1024+self.num_rec)] = runner.mon['r.V']
    V[:,32*1024 : (32*1024+self.num_out)] = runner.mon['o.V']

    wacc1 = np.zeros((8,96*1024))
    wacc1[:,0       : self.num_in]            = runner.mon['i2r.pron.syn.g']
    wacc1[:,16*1024 : (16*1024+self.num_rec)] = runner.mon['r2o.pron.syn.g']

    download_path = f"{download_path}/soft_data"
    download_dir = Path(download_path)
    download_dir.mkdir(exist_ok=True,parents=True)
    np.save(download_dir / "N_wacc1.npy", wacc1)
    np.save(download_dir / "N_V.npy", V)
    np.save(download_dir / "N_spike.npy", S)

    test = BrainpyBase(self, 0.)
    conn_matrix = test.get_connection_matrix()
    cv = test.cv
    with open(f'{download_dir}/connection.pickle', 'wb') as handle:
        pickle.dump(conn_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
  bm.set_dt(1.)
  num_in = 784
  num_rec = 128
  num_sample = 256
  num_step = 8
  bm.random.seed(42)

  mask = bm.random.rand(num_step, num_sample, num_in)
  inpS = bm.zeros((num_step, num_sample, num_in))
  inpS[mask < 0.01 ] = 1.0 #[T,B,N]
  target = bm.asarray(bm.random.rand(num_sample) < 0.5, dtype=bm.float_) #[B]

  # Batch mode
  with bm.training_environment():
      net = SNN(num_in, num_rec, 2)  
  runner = bp.DSRunner(net, data_first_axis='T', monitors=[],jit=False)
  outs = runner.run(inputs=inpS,reset_state=True) # must set reset_state=True if jit is enabled 
  outs = outs[-1,:,:]
  predict = bm.argmax(outs, axis=1)
  acc = bm.mean(target ==predict )  
  print("Accuracy %.3f" % acc)

  # None Batch mode
  # predict_list = []
  # for iSample in range(num_sample):
  #   net = SNN(num_in, num_rec, 2)  
  #   inpS_loc = inpS[:,iSample,:].astype(bool)
  #   target_loc = target[iSample]
  #   runner = bp.DSRunner(net, data_first_axis='T', monitors=[],jit=False)
  #   outs = runner.run(inputs=inpS_loc) #Set reset_state =True and move net init outside of forloop to accelerate
  #   outs = outs[-1,:]
  #   predict = bm.argmax(outs)
  #   predict_list.append(predict)
  # acc = bm.mean(target == bm.array(predict_list))  
  # print("Accuracy %.3f" % acc)

  net = SNN(num_in, num_rec, 2)  
  test = BrainpyBase(net, 0.)
  conn_matrix = test.get_connection_matrix()
  get_neuron_num = test.get_neuron_num()
  cv = test.cv
  V_init = test.Vinit