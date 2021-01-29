import numpy as np
from Individual import Individual
import math
import zdt3_utils


# Vectores peso (lambda)
# La suma de sus componentes debe ser 0 y tienen que estar uniformemente distribuidos
def generate_lambdas(N):
    lambdas = np.zeros([N,2])
    increment = np.array([1.0])/(np.array([N - 1.0]))
    x = np.array([0.0])

    for i in range(N):
        lambdas[i][0] = x
        lambdas[i][1] = 1.0 - x
        x = x + increment

    return lambdas


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
        individual = Individual(n,lambda_vector, t_neighbors)

        fx = zdt3_utils.zdt3(individual.x)
        # Update z
        if math.isnan(z[0]) or fx[0] <= z[0]:
            z[0] = fx[0]

        if math.isnan(z[1]) or fx[1] <= z[1]:
            z[1] = fx[1]

        population.append(individual)

    return population, z
