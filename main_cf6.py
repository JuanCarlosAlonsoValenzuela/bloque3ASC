import numpy as np
import cf6_utils
import differential_evolution
import matplotlib.pyplot as plt
import inicialization


# HYPERPARAMETERS
N = 40         # Population size
T = 5          # Neighborhood size
G = 40          # Number of generations
n = 30          # Number of dimensions

# DE hyperparameters
F = np.array([0.5])
CR = 0.5

# Paths
dat = 'PF/PF_cf6.dat'

# Get Pareto Front
pf_x, pf_y = cf6_utils.get_pf(dat)

# Gaussian hyperparameters
PR = 0.1
sigma = 0.05

# Get Pareto Front
pf_x, pf_y = cf6_utils.get_pf(dat)

##########################################################################

# Initial population and z
# sor stands for separation of objectives and restrictions
population, z = inicialization.initialize_population_cf6_sor(N, n, T)
f_1, f_2 = cf6_utils.get_representation(population, N)

# Representation of initial population
plt.title('Initial generation')
plt.plot(f_1, f_2, '.', color='b', label='Initial population')
plt.plot(pf_x, pf_y, '.', color='r', label='Pareto Front')
plt.plot(z[0], z[1], '*', color='g', label = 'z')
plt.show()

# plt.scatter(pf_x, pf_y, s=0.8, color='red')
# plt.show()


# Recibe una x y devuelve el resultado y las restricciones
