import numpy as np
from random import random
import zdt3


class Individual:
    def __init__(self, N, n, lambda_vector, t_neighbors):

        x = np.zeros((n,))
        for j in range(n):
            element = random()
            x[j] = element

        f = zdt3.zdt3(x, n)

        self.x = x                          # Individual of n dimensions (genotype)
        self.f_1 = f[0]                     # f_1 (phenotype)
        self.f_2 = f[1]                     # f_2 (phenotype)
        self.lambda_vector = lambda_vector  # lambda
        self.neighbors = t_neighbors        # B
        self.g = None                       # g TODO: Inicializar con un valor alto o suponiendo z = (f_1, f_2)

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