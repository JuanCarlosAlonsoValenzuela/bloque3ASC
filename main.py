import numpy as np
import matplotlib.pyplot as plt
from random import random
from random import seed
import zdt3
import init

# HYPERPARAMETERS:
N = 100         # Population size
T = 20          # Neighborhood size
G = 40          # Number of generations
n = 30          # Number of dimensions

# Seed random number generator
seed(1)

# Paths
dat = 'PF.dat'

# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)

population = init.generate_population(N, n)

f_1 = []
f_2 = []
for individual in population:
    out = zdt3.zdt3(individual, n)
    f_1.append(out[0])
    f_2.append(out[1])


plt.plot(f_1, f_2, '.', color='b')
plt.plot(pf_x, pf_y, '.', color='r')
plt.show()
