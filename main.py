import numpy as np
import matplotlib.pyplot as plt
from random import seed
import zdt3
import inicialization
import differential_evolution

# HYPERPARAMETERS:
N = 100         # Population size
T = 4          # Neighborhood size
G = 40          # Number of generations
n = 30          # Number of dimensions

# DE hyperparameters
F = 0.5
CR = 0.5

# Seed random number generator
# seed(2)     # TODO: Change

# Paths
dat = 'PF.dat'

# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)

##########################################################################
# TODO: Revisar que máximo y mínimo (1 y 0) no se violan al mutar o aplicar crossover
# Initial population and z
# TODO: Evaluar vecinos de generación inicial (g_te en función de los vecinos)
population, z = inicialization.initialize_population(N, n, T)

f_1, f_2 = zdt3.get_representation(population, N)

# TODO: Update Z
epoch = differential_evolution.differential_evolution(population, z, F, CR)

# PLOT
# plt.plot(f_1, f_2, '.', color='b')
# plt.plot(pf_x, pf_y, '.', color='r')
# plt.plot(z[0], z[1], '*', color='g')
# plt.show()


# TODO: TESTS
# Size of population is correct
