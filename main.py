import numpy as np
import matplotlib.pyplot as plt
from random import seed
import zdt3
import inicialization

# HYPERPARAMETERS:
N = 100         # Population size
T = 20          # Neighborhood size
G = 40          # Number of generations
n = 30          # Number of dimensions

# DE hyperparameters
F = 0.5
CR = 0.5

# Seed random number generator
seed(1)

# Paths
dat = 'PF.dat'

# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)

##########################################################################

# Initial population and z
population, z = inicialization.initialize_population(N, n, T)

# TODO: Evaluar vecinos de generación inicial (g_te en función de los vecinos)

# for individual in population: # TODO: Complete

f_1, f_2 = zdt3.get_representation(population, N)


print(population[0])
print(z)

# PLOT
plt.plot(f_1, f_2, '.', color='b')
plt.plot(pf_x, pf_y, '.', color='r')
plt.plot(z[0], z[1], '*', color='g')
plt.show()



# TODO: TESTS
# Size of population is correct
