import numpy as np
import matplotlib.pyplot as plt
import zdt3_utils
import differential_evolution
import inicialization
import pandas as pd
import os
from pathlib import Path
from random import seed
pd.set_option('precision', 8)


def main_class_zdt3(seed_number):
    # HYPERPARAMETERS:
    N = 200         # Population size
    T = 25          # Neighborhood size
    G = 50          # Number of generations
    n = 30          # Number of dimensions

    # DE hyperparameters
    F = np.array([0.5])
    CR = 0.5

    # Gaussian hyperparameters
    PR = 0.1
    sigma = 0.05

    # Paths
    dat = 'PF/PF_zdt3.dat'

    # Get Pareto Front
    pf_x, pf_y = zdt3_utils.get_pf(dat)

    ##########################################################################
    # Initial population and z
    population, z = inicialization.initialize_population_zdt3(N, n, T)
    f_1, f_2 = zdt3_utils.get_representation(population, N)

    # Initialize total_pop file
    total_pop = pd.DataFrame()

    plt.title('Generation {}'.format(0))
    plt.plot(f_1, f_2, '.', color='b', label='Initial population')
    plt.plot(pf_x, pf_y, '.', color='r', label='Pareto Front')
    plt.plot(z[0], z[1], '*', color='g', label='z')
    plt.show()

    i = 0
    while i < G:

        # Apply differential evolution
        population, z = differential_evolution.differential_evolution_zdt3(population, z, F, CR, sigma, PR)
        f_1, f_2 = zdt3_utils.get_representation(population, N)
        i = i + 1

        # Save current generation
        current_gen = pd.DataFrame()
        current_gen[0] = pd.Series(f_1)
        current_gen[1] = pd.Series(f_2)
        current_gen[2] = pd.Series(np.zeros([N]))

        # Concat previous generations with current one
        total_pop = pd.concat([total_pop, current_gen], axis=0, ignore_index=True)

        # if i % 100 == 0:
        #     plt.title('Generation {}'.format(i))
        #     plt.plot(f_1, f_2, '.', color='b')
        #     plt.scatter(pf_x, pf_y, color='r', s=0.8)
        #     plt.xlim([0.0, 1.0])
        #     plt.plot(z[0], z[1], '*', color='g')
        #     plt.show()

    # Write final generation
    n_eval = N*G
    final_folder = Path('zdt3_de_results/{}/P{}G{}'.format(n_eval, N, G))
    final_file_name = 'zdt3_final_popp{}g{}_seed{}.out'.format(N, G, seed_number)
    pop_file_name = 'zdt3_all_popmp{}g{}_seed{}.out'.format(N, G, seed_number)

    final_folder.mkdir(parents=True, exist_ok=True)
    final_path = os.path.join(final_folder, final_file_name)
    total_pop_path = os.path.join(final_folder, pop_file_name)

    final_pop = pd.DataFrame()
    final_pop[0] = pd.Series(f_1)
    final_pop[1] = pd.Series(f_2)
    final_pop[2] = pd.Series(np.zeros([N]))

    total_pop.to_csv(total_pop_path, sep='\t', header=False, index=False)
    final_pop.to_csv(final_path, sep='\t', header=False, index=False)

    plt.title('Final Generation')
    plt.plot(f_1, f_2, '.',color='b')
    plt.scatter(pf_x, pf_y, color='r', s=0.8)
    plt.plot(z[0], z[1], '*', color='g')
    plt.show()


# Seed random number generator
for seed_value in range(1, 11):
    main_class_zdt3(seed_value)
