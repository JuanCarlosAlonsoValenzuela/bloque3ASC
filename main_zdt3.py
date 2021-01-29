import numpy as np
import matplotlib.pyplot as plt
import zdt3_utils as zdt3_utils
import differential_evolution as differential_evolution
import inicialization as inicialization


def main_class():
    # HYPERPARAMETERS:
    N = 100         # Population size
    T = 15          # Neighborhood size
    G = 40          # Number of generations
    n = 30          # Number of dimensions

    # DE hyperparameters
    F = np.array([0.5])
    CR = 0.5

    # Gaussian hyperparameters
    PR = 0.1

    # Gaussian hyperparameters
    sigma = 0.05

    # Paths
    dat = 'PF/PF_zdt3.dat'

    # Get Pareto Front
    pf_x, pf_y = zdt3_utils.get_pf(dat)

    ##########################################################################
    # Initial population and z
    population, z = inicialization.initialize_population(N, n, T)
    f_1, f_2 = zdt3_utils.get_representation(population, N)

    plt.title('Generation {}'.format(0))
    plt.plot(f_1, f_2, '.', color='b', label='DE with Gaussian mutation')
    plt.plot(pf_x, pf_y, '.', color='r', label='Pareto Front')
    plt.plot(z[0], z[1], '*', color='g', label = 'z')
    plt.show()

    i = 0
    while i < G:

        # Apply differential evolution
        population, z = differential_evolution.differential_evolution(population, z, F, CR, sigma, PR)

        f_1, f_2 = zdt3_utils.get_representation(population, N)

        i = i + 1

        if i%10 == 0:
            plt.title('Generation {}'.format(i))
            plt.plot(f_1, f_2, '.', color='b')
            plt.scatter(pf_x, pf_y, color='r', s=0.8)
            plt.xlim([0.0, 1.0])
            plt.plot(z[0], z[1], '*', color='g')
            plt.show()

    plt.title('Final Generation')
    plt.scatter(f_1, f_2, color='b', s=0.8)
    plt.scatter(pf_x, pf_y, color='r', s=0.8)
    plt.plot(z[0], z[1], '*', color='g')
    plt.show()


# Seed random number generator
main_class()
