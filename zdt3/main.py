import numpy as np
import matplotlib.pyplot as plt
from random import seed
from zdt3.zdt3 import differential_evolution, Individual, inicialization, zdt3


def main_class():
    # HYPERPARAMETERS:
    N = 100         # Population size
    T = 20          # Neighborhood size
    G = 100        # Number of generations
    n = 30          # Number of dimensions

    # DE hyperparameters
    F = np.array([0.5])
    CR = 0.5

    # Gaussian hyperparameters
    PR = 0.1

    # Gaussian hyperparameters
    sigma = 0.05

    # Paths
    dat = 'PF.dat'

    # Get Pareto Front
    pf_x, pf_y = zdt3.get_pf(dat)

    ##########################################################################
    # Initial population and z
    population, z = inicialization.initialize_population(N, n, T)


    f_1, f_2 = zdt3.get_representation(population, N)
    zero_individual = population[N - 1]
    print('F: {}'.format(zdt3.zdt3(zero_individual.x)))
    print('Lambda: {}'.format(zero_individual.lambda_vector))
    print('G: {}'.format(Individual.compute_g(zdt3.zdt3(zero_individual.x), zero_individual.lambda_vector, z)))
    print('Z: {}'.format(z))
    print(100 * '#')
    plt.title('Generation {}'.format(0))

    plt.plot(f_1, f_2, '.', color='b')
    # plt.plot(f_1[N - T:N-1], f_2[N-T:N - 1], 'o', color='r')
    # plt.plot(f_1[N-1], f_2[N-1], 'o', color='g')
    plt.scatter(pf_x, pf_y, color='r', s=0.8)
    plt.plot(z[0], z[1], '*', color='g')
    plt.show()

    # print(population[0])
    weight = 0

    print(100*'#')

    # f_1, f_2 = zdt3.get_representation(population, N)

    # TODO: Update Z
    i = 0
    while i < G:
        # PLOT
        #if i%10==0:
        #zdt3.get_representation_of_weights(population[39])    # TODO: USE
        # plt.plot(f_1[0], f_2[0], '.', color='r')
        # plt.plot(f_1[98], f_2[98], 'o', color='g')
        # print(population[N-1])
        # plt.plot(f_1[1:3], f_2[1:3], 'o', color='purple')
        # plt.scatter(f_1[5:], f_2[5:], color='b', s=0.5)
        differential_evolution.differential_evolution(population, z, F, CR, sigma, PR)

        f_1, f_2 = zdt3.get_representation(population, N)

        i = i + 1

        if i%20 == 0:
            zero_individual = population[N - 1]
            print('F: {}'.format(zdt3.zdt3(zero_individual.x)))
            print('Lambda: {}'.format(zero_individual.lambda_vector))
            print('G: {}'.format(Individual.compute_g(zdt3.zdt3(zero_individual.x), zero_individual.lambda_vector, z)))
            print('Z: {}'.format(z))
            print(100 * '#')
            plt.title('Generation {}'.format(i))

            plt.plot(f_1, f_2, '.', color='b')
            # plt.plot(f_1[N - T:N - 1], f_2[N - T:N - 1], 'o', color='r')
            # plt.plot(f_1[N - 1], f_2[N - 1], 'o', color='g')
            plt.scatter(pf_x, pf_y, color='r', s=0.8)
            plt.plot(z[0], z[1], '*', color='g')
            plt.show()


        # zdt3.get_representation_of_all_weights(population)

        # TODO: Consider decay



    plt.title('Final Generation')
    plt.scatter(f_1, f_2, color='b', s=0.8)
    plt.scatter(pf_x, pf_y, color='r', s=0.8)
    plt.plot(z[0], z[1], '*', color='g')
    plt.show()
    for element in population:
        print(element)
    print(z)


# Seed random number generator
seed(0)     # TODO: Remove seed from all classes
main_class()

seed(1)
main_class()

seed(2)
main_class()
