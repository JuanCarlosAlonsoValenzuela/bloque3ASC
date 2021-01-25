import numpy as np
from Individual import Individual
import math


# Vectores peso (lambda)
# La suma de sus componentes debe ser 0 y tienen que estar uniformemente distribuidos
def generate_lambdas(N):
    lambdas = np.zeros([N,2])
    increment = np.array([1.0])/(np.array([N - 1.0]))
    x = np.array([0.0])
    i = 0
    while x <= 1.0:
        # lambdas[0][i] = np.array([x, 1.0 - x])
        lambdas[i][0] = x
        lambdas[i][1] = 1.0 - x
        x = x + increment
        i = i + 1

    return lambdas


def initialize_population(N, n, T):
    population = []
    lambdas = generate_lambdas(N)
    # print(lambdas)

    # z vector
    z = np.zeros((2,))
    z[:] = np.nan

    for lambda_vector in lambdas:
        # Obtain T neighbors of lambda vector (B)
        dist = np.linalg.norm(lambdas - lambda_vector, ord=2, axis=1)
        t_neighbors = lambdas[np.argsort(dist)][:T]

        # Create new individual
        individual = Individual(N, n,lambda_vector, t_neighbors)

        # Update z
        if math.isnan(z[0]) or individual.fx[0] < z[0]:
            z[0] = individual.fx[0]

        if math.isnan(z[1]) or individual.fx[1] < z[1]:
            z[1] = individual.fx[1]

        population.append(individual)

    # Initialize gx
    for individual in population:
        individual.initialize_g(z)

    return population, z
