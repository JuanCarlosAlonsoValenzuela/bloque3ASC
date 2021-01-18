import numpy as np
from random import random

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


def get_lambdas_with_neighbors(lambdas, T):
    lambdas_with_neighbors = {}
    for element in lambdas:
        dist = np.linalg.norm(lambdas - element, ord=2, axis=1)
        t_neighbors = lambdas[np.argsort(dist)]
        lambdas_with_neighbors[tuple(element)] = t_neighbors[:T]

    return lambdas_with_neighbors


def generate_population(N, n):
    population = np.zeros((N, n))

    for i in range(N):
        x = np.zeros((n,))
        for j in range(n):
            element = random()
            x[j] = element
        population[i] = x

    return population




# # TODO: DELETE
# lambdas_res = generate_lambdas(5)
# print(lambdas_res)
# lambdas_res_with_predicates = get_lambdas_with_neighbors(lambdas_res, 5)
# print(lambdas_res_with_predicates)
