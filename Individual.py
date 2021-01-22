import numpy as np
from random import random
import zdt3


class Individual:
    def __init__(self, N, n, lambda_vector, t_neighbors):

        x = np.zeros((n,))
        for j in range(n):
            element = random()
            x[j] = element

        f = zdt3.zdt3(x)
        # TODO CHANGE TO NUMPY SCALARS
        self.x = x                          # Individual of n dimensions (genotype)
        self.f_1 = f[0]                     # f_1 (phenotype)
        self.f_2 = f[1]                     # f_2 (phenotype)
        self.lambda_vector = lambda_vector  # lambda
        self.neighbors = t_neighbors        # B
        self.g = None                       # g TODO: Inicializar con un valor alto o suponiendo z = (f_1, f_2)
        self.y = np.zeros((n,))

    def initialize_g(self, z):

        f_vector = np.array([self.f_1, self.f_2])
        self.g = compute_g(f_vector, self.lambda_vector, z)

    def __str__(self):

        r = """ 
x: {}
f: ({},{})
lambda: {}
neighbors: {}
g: {}
""".format(self.x, self.f_1, self.f_2,
                   self.lambda_vector, self.neighbors,self.g)

        return r


def compute_g(f, lambdas, z):

    g_1 = lambdas[0] * abs(f[0] - z[0])
    g_2 = lambdas[1] * abs(f[1] - z[1])

    return max(g_1, g_2)