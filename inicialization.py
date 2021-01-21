import numpy as np
from random import random
from Individual import Individual
import math


# Vectores peso (lambda)
# La suma de sus componentes debe ser 0 y tienen que estar uniformemente distribuidos
def generate_lambdas(N):
    lambdas = []
    increment = 1.0/(N - 1.0)
    x = 0.0
    while x <= 1.0:
        lambdas.append([x, 1.0 - x])
        x = round(x + increment, 10)

    return np.array(lambdas)


def initialize_population(N, n, T):
    population = []
    lambdas = generate_lambdas(N)

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
        if math.isnan(z[0]) or individual.f_1 < z[0]:
            z[0] = individual.f_1

        if math.isnan(z[1]) or individual.f_2 < z[1]:
            z[1] = individual.f_2

        population.append(individual)

    return population, z
