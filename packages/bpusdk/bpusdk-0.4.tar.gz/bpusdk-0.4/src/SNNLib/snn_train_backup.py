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


class Trainer:
  def __init__(self, net, opt,num_step):
    self.net = net
    self.opt = opt
    self.num_step = num_step
    opt.register_train_vars(net.train_vars().unique())
    self.f_grad = bm.grad(self.f_loss, grad_vars=self.opt.vars_to_train, return_value=True, has_aux=True)

  def f_loss(self,x_data,y_data):
    self.net.reset(num_sample)
    indices = bm.arange(self.num_step)
    outs = bm.for_loop(self.net.step_run, (indices, x_data)) #[T,B,N]
    outs = outs[-1,:,:]
    #predict = bm.max(outs, axis=0)
    loss = bp.losses.cross_entropy_loss(outs, y_data)
    predict = bm.argmax(outs, axis=1)
    acc = bm.mean(y_data ==predict )  # compare to labels
    return (loss,acc)

  @bm.cls_jit
  def f_train(self,x_data,y_data):
    grads, loss,acc = self.f_grad(x_data,y_data)
    self.opt.update(grads)
    
    return loss,acc

class SNN(bp.DynamicalSystem):
  def __init__(self, num_in, num_rec, num_out):
    super().__init__()

    # parameters
    self.num_in = num_in
    self.num_rec = num_rec
    self.num_out = num_out

    # neuron groups
    self.o = bp.dyn.Integrator(num_out, tau=10.)

    # synapse: r->o
    self.r2o = bp.Sequential(
        comm=bp.dnn.Linear(num_rec, num_out, W_initializer=bp.init.KaimingNormal(scale=20.), b_initializer=None),
        syn=bp.dyn.Expon(num_out, tau=10.,method="euler"), 
    )

  def update(self, spike):

    tmp1 = self.i2r(spike)
    tmp2 = self.r(tmp1)
    tmp3 = self.r2o(tmp2)
    tmp4 = self.o(tmp3)

    #output = spike >> self.i2r >> self.r >> self.r2o >> self.o
    return tmp4

bm.set_dt(1.)
num_in = 784
num_rec = 128
num_sample = 256
num_step = 8
num_class = 2
bm.random.seed(42)

mask = bm.random.rand(num_step, num_sample, num_in)
x_data = bm.zeros((num_step, num_sample, num_in))
x_data[mask < 0.01 ] = 1.0 #[T,B,N]
y_data = bm.asarray(bm.random.rand(num_sample) < 0.5, dtype=bm.float_) #[B]

with bm.training_environment():
    net = SNN(num_in, num_rec, num_class)  # out task is a two label classification task
trainer = Trainer(net=net, opt=bp.optim.Adam(lr=4e-3),num_step=num_step)
for iEpoch in range(30):
  loss,acc = trainer.f_train(x_data,y_data)
  print(f'Train {iEpoch + 1} iEpoch, loss {loss}, acc{acc}')


# runner = bp.DSRunner(net, data_first_axis='T',monitors=[],jit=False)
# outs = runner.run(inputs=x_data)
# outs = outs[-1,:,:]
# predict = bm.argmax(outs, axis=1)
# acc = bm.mean(y_data ==predict )  # compare to labels
# print("Accuracy %.3f" % acc)
# np.save("./i2r_W.npy",np.array(net.i2r.comm.W))
# np.save("./r2o_W.npy",np.array(net.r2o.comm.W))
