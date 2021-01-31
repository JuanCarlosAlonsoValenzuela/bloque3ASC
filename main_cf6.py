import numpy as np
import cf6_utils
import differential_evolution
import matplotlib.pyplot as plt
import inicialization
import pandas as pd
import os
from pathlib import Path
pd.set_option('precision', 8)


def main_class_cf6(seed_number):
    # HYPERPARAMETERS
    N = 200         # Population size
    T = 25          # Neighborhood size
    G = 50         # Number of generations
    n = 16          # Number of dimensions

    # DE hyperparameters
    F = np.array([0.5])
    CR = 0.5

    # Paths
    dat = 'PF/PF_cf6.dat'

    # Get Pareto Front
    pf_x, pf_y = cf6_utils.get_pf(dat)

    # Gaussian hyperparameters
    PR = 0.3
    sigma = 0.05

    ##########################################################################

    # Initial population and z
    # sor stands for separation of objectives and restrictions
    population, z = inicialization.initialize_population_cf6_sor(N, n, T)
    f_1, f_2, constr_1, constr_2 = cf6_utils.get_representation(population, N)

    # Initialize total_pop file
    total_pop = pd.DataFrame()

    # Representation of initial population
    plt.title('Initial generation')
    plt.plot(f_1, f_2, '.', color='b', label='Initial population')
    plt.plot(pf_x, pf_y, '.', color='r', label='Pareto Front')
    # plt.plot(pf_x_zdt3, pf_y_zdt3, '.', color='g', label='Pareto Front')
    plt.plot(z[0], z[1], '*', color='g', label = 'z')
    plt.show()

    i = 0
    while i < G:
        # Apply differential evolution
        population, z = differential_evolution.differential_evolution_cf6(population, z, F, CR, sigma, PR)
        f_1, f_2, constr_1, constr_2 = cf6_utils.get_representation(population, N)
        i = i + 1

        # Save current generation
        current_gen = pd.DataFrame()
        current_gen[0] = pd.Series(f_1)
        current_gen[1] = pd.Series(f_2)
        current_gen[2] = pd.Series(constr_1)
        current_gen[3] = pd.Series(constr_2)

        total_pop = pd.concat([total_pop, current_gen], axis=0, ignore_index=True)

        # if i%10 == 0:
        #     plt.title('Generation {}'.format(i))
        #     plt.plot(f_1, f_2, '.', color='b')
        #     plt.scatter(pf_x, pf_y, color='r', s=0.8)
        #     # plt.plot(pf_x_zdt3, pf_y_zdt3, '.', color='g', label='Pareto Front')
        #     plt.plot(z[0], z[1], '*', color='g')
        #     plt.show()

    # Prepare folders and files
    n_eval = N*G
    final_folder = Path('cf6_{}d_de_results/{}/P{}G{}'.format(n, n_eval, N, G))
    final_file_name = 'cf6_{}d_final_popp{}g{}_seed{}.out'.format(n, N, G, seed_number)
    pop_file_name = 'cf6_{}d_all_popmp{}g{}_seed{}.out'.format(n, N, G, seed_number)

    final_folder.mkdir(parents=True, exist_ok=True)
    final_path = os.path.join(final_folder, final_file_name)
    total_pop_path = os.path.join(final_folder, pop_file_name)

    # Write final generation
    final_pop = pd.DataFrame()
    final_pop[0] = pd.Series(f_1)
    final_pop[1] = pd.Series(f_2)
    final_pop[2] = pd.Series(constr_1)
    final_pop[3] = pd.Series(constr_2)

    total_pop.to_csv(total_pop_path, sep='\t', header=False, index=False)
    final_pop.to_csv(final_path, sep='\t', header=False, index=False)

    plt.title('Final Generation')
    plt.plot(f_1, f_2, '.', color='b')
    plt.scatter(pf_x, pf_y, color='r', s=0.8)
    plt.plot(z[0], z[1], '*', color='g')
    plt.show()


# Recibe una x y devuelve el resultado y las restricciones
# for seed_value in range(1, 11):
#     main_class_cf6(seed_value)
