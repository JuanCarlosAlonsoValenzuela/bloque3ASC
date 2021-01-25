import numpy as np
import matplotlib.pyplot as plt
from random import seed
import zdt3
import inicialization
import differential_evolution

# HYPERPARAMETERS:
N = 100         # Population size
T = 15          # Neighborhood size
G = 1000        # Number of generations
n = 30          # Number of dimensions

# DE hyperparameters
F = np.array([0.5])
CR = 0.5

# Gaussian hyperparameters
PR = 0.05

# Gaussian hyperparameters
sigma = 0.05

# Seed random number generator
# seed(0)     # TODO: Change

# Paths
dat = 'PF.dat'

# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)

##########################################################################
# Initial population and z
population, z = inicialization.initialize_population(N, n, T)

# z = np.array([0.0, -10.0])

# f_1, f_2 = zdt3.get_representation(population, N)

# TODO: Update Z
i = 0
while i < G:
    # print(F)
    # if i % 50 == 0:
    #     print(i)
    if i % 10 == 0:
        f_1, f_2 = zdt3.get_representation(population, N)
        # PLOT
        plt.title('Generation {}'.format(i))
        plt.scatter(f_1, f_2, color='b', s=0.8)
        plt.scatter(pf_x, pf_y, color='r', s=0.8)
        plt.plot(z[0], z[1], '*', color='g')
        plt.show()

    differential_evolution.differential_evolution(population, z, F, CR, sigma, PR)

    # DECAY (OPTIONAL)
    # if (i % 50 == 0) and (F >= 0.2):
    #     F = F - 0.05
    # if (i% 20 == 0) and (CR >= 0.4):
    #     CR = CR - 0.1
    i = i+1

plt.title('Final Generation')
plt.scatter(f_1, f_2, color='b', s=0.8)
plt.scatter(pf_x, pf_y, color='r', s=0.8)
plt.plot(z[0], z[1], color='g')
plt.show()
# for element in population:
#     print(element)
# print(z)

# TODO: TESTS
# Size of population is correct
