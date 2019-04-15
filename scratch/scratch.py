# %%
from matplotlib import pyplot as plt
import numpy as np

fx = np.arange(0, 1.01, .01)
one_fx = 1 - fx
y = 1 / (fx * one_fx)[1: -1]

fig = plt.figure()
plt.scatter(fx[1:-1], y)
plt.xlabel('cdf F(x)', fontsize=16)
plt.ylabel(r'$\frac{1}{F(x)  (1 - F(x))}$', fontsize=16)
plt.savefig('./static/images/anderson_weight.png')