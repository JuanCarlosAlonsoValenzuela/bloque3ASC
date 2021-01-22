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

    def update_x(self, new_x, new_g):
        self.x = new_x
        self.fx = zdt3.zdt3(new_x)
        self.gx = new_g

    def initialize_g(self, z):
        self.gx = compute_g(self.fx, self.lambda_vector, z)

    def add_and_evaluate_y(self, y_vector):
        self.y = y_vector
        return zdt3.zdt3(y_vector)

    def get_neighbors_of_individual(self, population):
        neighbors_res = []
        for neighbor_candidate in population:
            if neighbor_candidate.lambda_vector in self.neighbors:
                neighbors_res.append(neighbor_candidate)
        return neighbors_res

    def compare_with_vector(self, vector, z):
        f = zdt3.zdt3(vector)
        g = compute_g(f, self.lambda_vector, z)

        # Update x (and derivates) if g<self.gx
        if g < self.gx:
            self.update_x(vector, g)

    def __str__(self):
        r = 'x: {} \n' \
            'f: {} \n' \
            'lambda: {} \n' \
            'neighbors: {} \n' \
            'gx: {}'.format(self.x, self.fx,
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
