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

##########################################################################

# Initial population
population = init.generate_population(N, n)     # x vectors (genotype)

f_1 = np.zeros([100, 1])        # F1 (phenotype)
f_2 = np.zeros([100, 1])        # F2 (phenotype)
for i in range(len(population)):
    individual = population[i]
    out = zdt3.zdt3(individual, n)
    f_1[i] = out[0]
    f_2[i] = out[1]

# Inital values of z
z = np.array([np.amin(f_1), np.amin(f_2)])

# Identify B (nearest neighbors)
B = init.get_neighbors(N, T)


# PLOT
plt.plot(f_1, f_2, '.', color='b')
plt.plot(pf_x, pf_y, '.', color='r')
plt.plot(z[0], z[1], '*', color='g')
plt.show()
