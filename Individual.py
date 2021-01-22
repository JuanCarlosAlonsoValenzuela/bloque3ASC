import numpy as np
from random import random
import zdt3


class Individual:
    def __init__(self, N, n, lambda_vector, t_neighbors):

        x = np.zeros((n,))
        for j in range(n):
            element = random()
            x[j] = element

        # TODO CHANGE TO NUMPY SCALARS
        self.x = x                          # Individual of n dimensions (genotype)
        self.fx = zdt3.zdt3(x)              # f(x) (phenotype)
        self.lambda_vector = lambda_vector  # lambda
        self.neighbors = t_neighbors        # B
        self.gx = None                       # gx TODO: Inicializar con un valor alto o suponiendo z = (f_1, f_2)
        self.y = np.zeros((n,))
        self.fy = None

    def initialize_g(self, z):
        self.gx = compute_g(self.fx, self.lambda_vector, z)

    def add_and_evaluate_y(self, y_vector):
        self.y = y_vector
        self.fy = zdt3.zdt3(y_vector)

    def __str__(self):

        r = """ 
x: {}
f: {}
lambda: {}
neighbors: {}
gx: {}
""".format(self.x, self.fx,
           self.lambda_vector, self.neighbors, self.gx)

        return r


def compute_g(f, lambdas, z):

    g_1 = lambdas[0] * abs(f[0] - z[0])
    g_2 = lambdas[1] * abs(f[1] - z[1])

    return max(g_1, g_2)


def check_lower_and_upper_limit(vector):
    for i in range(vector.shape[0]):
        if vector[i] < 0.0:
            vector[i] = 0.0
        if vector[i] > 1.0:
            vector[i] = 1.0
