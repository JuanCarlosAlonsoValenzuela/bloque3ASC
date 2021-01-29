import numpy as np
import random
from random import randint
import Individual as Individual


def differential_evolution_zdt3(population, z, F, CR, sigma, PR):
    for individual_1 in population:
        # STEP 1: REPRODUCTION
        # Select 3 random neighbors (lambdas)
        lambda_selected_neighbors = individual_1.neighbors.copy()
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

        # MUTATION Generate mutant vector
        v_g1 = x_r1 + F * (x_r2 - x_r3)

        # CROSSOVER to increase diversity
        # generate y
        # Check lower and upper value
        u_g1 = generate_crossover(individual_1.x.copy(), v_g1, CR)
        Individual.check_lower_and_upper_limit_zdt3(u_g1)

        # Mutate with gaussian distribution
        Individual.mutate_with_gaussian_distribution_zdt3(u_g1, sigma, PR)

        # STEP 2: EVALUATION
        # This function changes the value of y and computes the value of F(y)
        fy = individual_1.add_and_evaluate_y_zdt3(u_g1.copy())

        # STEP 3: UPDATE Z
        if fy[0] <= z[0]:
            z[0] = fy[0].copy()
        if fy[1] <= z[1]:
            z[1] = fy[1].copy()

    # STEP 4: UPDATE NEIGHBORS
    for candidate in population:
        y = candidate.y.copy()

        # Compare with neighbors
        neighbors_of_individual = candidate.get_neighbors_of_individual(population)
        for single_neighbor in neighbors_of_individual:
            single_neighbor.compare_with_vector_zdt3(y.copy(), z)

    return population, z


def generate_crossover(x, v, CR):
    delta = randint(0, x.shape[0] - 1)  # random integer (min: 0, max: n-1)
    u = np.zeros(x.shape)

    for i in range(x.shape[0]):
        random_value = random.uniform(0, 1)

        if (random_value <= CR) or (delta == i):
            u[i] = v[i]
        else:
            u[i] = x[i]
    return u


def differential_evolution_cf6(population, z, F, CR, sigma, PR):
    for individual_1 in population:
        # STEP 1: REPRODUCTION
        # Select 3 random neighbors (lambdas)
        lambda_selected_neighbors = individual_1.neighbors.copy()
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

        # MUTATION Generate mutant vector
        v_g1 = x_r1 + F * (x_r2 - x_r3)

        # CROSSOVER to increase diversity
        # generate y
        # Check lower and upper value
        u_g1 = generate_crossover(individual_1.x.copy(), v_g1, CR)
        # Change upper and lower limits
        Individual.check_lower_and_upper_limit_cf6(u_g1)

        # Mutate with gaussian distribution (and check limits)
        # Limits
        # i = 0 -->     min= 0.0,   max=1.0
        # i > 0 -->     min= -2.0,  max=2.0
        Individual.mutate_with_gaussian_distribution_cf6(u_g1, sigma, PR)

        # STEP 2: EVALUATION
        # This function changes the value of y and computes the value of F(y)
        fy, constry = individual_1.add_and_evaluate_y_cf6(u_g1.copy())

        # STEP 3: UPDATE Z
        if fy[0] <= z[0]:
            z[0] = fy[0].copy()
        if fy[1] <= z[1]:
            z[1] = fy[1].copy()

    # STEP 4: UPDATE NEIGHBORS
    for candidate in population:
        y = candidate.y.copy()

        # Compare with neighbors
        neighbors_of_individual = candidate.get_neighbors_of_individual(population)
        for single_neighbor in neighbors_of_individual:
            # Compare with neighbor (considering Separation of constraints and objectives)
            single_neighbor.compare_with_vector_cf6(y.copy(), z)

    return population, z
