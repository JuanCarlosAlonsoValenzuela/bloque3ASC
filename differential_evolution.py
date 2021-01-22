import numpy as np
from random import random
from random import randint
import zdt3
import Individual


def differential_evolution(population, z, F, CR):
    # TODO: Convert to for loop
    individual = population[0]

    # Select 3 random neighbors (lambdas)
    lambda_selected_neighbors = individual.neighbors.copy()
    np.random.shuffle(lambda_selected_neighbors)
    lambda_selected_neighbors = lambda_selected_neighbors[0:3]

    # Obtain individuals associated to the selected lambdas
    selected_neighbors = []
    for neighbor_candidate in population:
        if neighbor_candidate.lambda_vector in lambda_selected_neighbors:
            selected_neighbors.append(neighbor_candidate)

    # Compute next generation
    x_r1 = selected_neighbors[0].x
    x_r2 = selected_neighbors[1].x
    x_r3 = selected_neighbors[2].x

    # MUTATION Generate mutant vector   TODO: upper and lower limits
    v_g1 = x_r1 + F * (x_r2 - x_r3)

    # CROSSOVER to increase diversity
    delta = randint(0, x_r1.shape[0] - 1)   # random integer (min: 0, max: 29)

    # generate y
    # TODO: Check upper (1.0) and lower (0.0) limits
    u_g1 = generate_crossover(x_r1, v_g1, CR)

    # SELECTION: decide if trial vector (u_g1) enters the population
    # 2.-Evaluation Compute F(y)
    f_ug1 = zdt3.zdt3(u_g1)
    # Evaluate F(y) (ie. Compute g)
    g_ug1 = Individual.compute_g(f_ug1, individual.lambda_vector, z)

    # Update z
    # If g is smaller, replace x with u_g1
    # if g_ug1 < individual.g:

    # If replace, check usability for neighbors
    # TODO: Update f_1 and f_2
    # TODO: Second mutation (gauss)
    # TODO: Compare with neighbors (G)

    # TODO: Update z (This must be done at the end of a generation)

    return None


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






