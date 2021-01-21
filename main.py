import numpy as np
import matplotlib.pyplot as plt
from random import random
from random import seed
import zdt3
import inicialization

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

# Initial population and z
population, z = inicialization.initialize_population(N, n, T)

f_1 = np.zeros([N, 1])        # F1 (phenotype)
f_2 = np.zeros([N, 1])        # F2 (phenotype)
for i in range(N):
    individual = population[i]
    # out = zdt3.zdt3(individual, n)
    f_1[i] = individual.f_1
    f_2[i] = individual.f_2

# Inital values of z (Minimum values)
z = np.array([np.amin(f_1), np.amin(f_2)])

print(population[0])

# PLOT
plt.plot(f_1, f_2, '.', color='b')
plt.plot(pf_x, pf_y, '.', color='r')
plt.plot(z[0], z[1], '*', color='g')
plt.show()

# TODO: TESTS
# Size of population is correct

