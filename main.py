import numpy as np
import matplotlib.pyplot as plt
from random import seed
import zdt3
import inicialization
import differential_evolution

# HYPERPARAMETERS:
N = 100         # Population size
T = 15          # Neighborhood size
G = 100        # Number of generations
n = 30          # Number of dimensions

# DE hyperparameters
F = np.array([0.5])
CR = 0.5

# Gaussian hyperparameters
PR = 0.05

# Gaussian hyperparameters
sigma = 0.05

# Seed random number generator
seed(0)     # TODO: Remove seed from all classes

# Paths
dat = 'PF.dat'

# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)

##########################################################################
# Initial population and z
population, z = inicialization.initialize_population(N, n, T)


print(population[0])
weight = 0

print(100*'#')

# f_1, f_2 = zdt3.get_representation(population, N)

# TODO: Update Z
i = 0
while i < G:
    f_1, f_2 = zdt3.get_representation(population, N)
    # PLOT
    # print(population[39])
    # if i%10==0:
    # zdt3.get_representation_of_weights(population[39])    # TODO: USE
    print(z)
    plt.title('Generation {}'.format(i))
    # plt.plot(f_1[0], f_2[0], '.', color='r')
    plt.plot(f_1[98], f_2[98], 'o', color='g')
    print(population[0])
    # plt.plot(f_1[1:3], f_2[1:3], 'o', color='purple')
    # plt.scatter(f_1[5:], f_2[5:], color='b', s=0.5)
    plt.plot(f_1[0:39], f_2[0:39], '.', color='b')
    plt.scatter(pf_x, pf_y, color='r', s=0.8)
    plt.plot(z[0], z[1], '*', color='g')
    # plt.ylim(-0.8,6.0)
    plt.show()

    differential_evolution.differential_evolution(population, z, F, CR, sigma, PR)
    # zdt3.get_representation_of_all_weights(population)

    # TODO: Consider decay

    i = i+1

plt.title('Final Generation')
plt.scatter(f_1, f_2, color='b', s=0.8)
plt.scatter(pf_x, pf_y, color='r', s=0.8)
plt.plot(z[0], z[1], '*', color='g')
plt.show()
for element in population:
    print(element)
print(z)

# TODO: TESTS
# Size of population is correct
