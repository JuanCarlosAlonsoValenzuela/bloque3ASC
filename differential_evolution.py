import numpy as np
from random import random
from random import randint
import zdt3
import Individual


def differential_evolution(population, z, F, CR, sigma, PR):
    # TODO: Add second mutation
    for individual in population:
        # STEP 1: REPRODUCTION
        # Select 3 random neighbors (lambdas)
        lambda_selected_neighbors = individual.neighbors.copy()
        np.random.shuffle(lambda_selected_neighbors)
        lambda_selected_neighbors = lambda_selected_neighbors[0:3]

        # Obtain individuals (complete object) associated to the selected lambdas
        selected_neighbors = []
        for neighbor_candidate in population:
            if neighbor_candidate.lambda_vector in lambda_selected_neighbors:
                selected_neighbors.append(neighbor_candidate)

        # Compute next generation
        x_r1 = selected_neighbors[0].x.copy()
        x_r2 = selected_neighbors[1].x.copy()
        x_r3 = selected_neighbors[2].x.copy()

        # TODO: APPLY GAUSSIAN MUTATION BEFORE
        # MUTATION Generate mutant vector
        v_g1 = x_r1 + F * (x_r2 - x_r3)
        # Check lower and upper value
        Individual.check_lower_and_upper_limit(v_g1)


        # CROSSOVER to increase diversity

        # generate y
        # Check lower and upper value
        u_g1 = generate_crossover(individual.x.copy(), v_g1, CR)           # TODO: Individual es x, antes era x_r1
        Individual.check_lower_and_upper_limit(u_g1)
        # Mutate with gaussian distribution

        Individual.mutate_with_gaussian_distribution(u_g1, sigma, PR)

        # STEP 2: EVALUATION
        # This function changes the value of y and computes the value of F(y)
        fy = individual.add_and_evaluate_y(u_g1.copy())

        # STEP 3: UPDATE Z
        if fy[0] < z[0]:
            z[0] = fy[0].copy()
        if fy[1] < z[1]:
            z[1] = fy[1].copy()

    # STEP 4: UPDATE NEIGHBORS
    for individual in population:
        y = individual.y.copy()

        # TODO: After (do not compare with neighbors)
        # individual.compare_with_vector(y, z)
        # TODO: Before (compare with all neighbors)
        neighbors_of_individual = individual.get_neighbors_of_individual(population)
        # Para cada vecino,  comprobar si g es mejor, en caso afirmativo, reemplazar x por y
        for single_neighbor in neighbors_of_individual:
            # Updates the value of x of the neighbor if new_g < old_g
            single_neighbor.compare_with_vector(y, z)

    # TODO: Second mutation (gauss)
    # TODO: Compare with neighbors (G)


def generate_crossover(x, v, CR):

    delta = randint(0, x.shape[0] - 1)  # random integer (min: 0, max: n-1)
    u = np.zeros(x.shape)

    for i in range(x.shape[0]):
        random_value = random()

        if (random_value <= CR) or (delta == i):
            u[i] = v[i]
        else:
            u[i] = x[i]
    return u






