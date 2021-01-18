import numpy as np
import matplotlib.pyplot as plt
from random import random
from random import seed
import zdt3

# HYPERPARAMETERS:
N = 100         # Population size
T = 30          # Neighborhood size
G = 40          # Number of generations

dat = 'PF.dat'

# Seed random number generator
seed(1)
n = 30
f_1 = []
f_2 = []
for i in range(N):
    w = []
    for j in range(n):
        element = random()
        w.append(random())

    out2 = zdt3.zdt3(w, n)
    f_1.append(out2[0])
    f_2.append(out2[1])

# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)


plt.plot(f_1, f_2, '.', color='b')
plt.plot(pf_x, pf_y, '.', color='r')
plt.show()
