import numpy as np
import random
from zdt3 import zdt3_utils

# random.seed(0)

class Individual:
    def __init__(self, N, n, lambda_vector, t_neighbors):

        x = np.zeros((n,))
        for j in range(n):
            element = random.random()
            x[j] = element

        # TODO CHANGE TO NUMPY SCALARS
        self.x = x                          # Individual of n dimensions (genotype)
        self.lambda_vector = lambda_vector  # lambda
        self.neighbors = t_neighbors        # B
        self.y = np.zeros((n,))

    def update_x(self, new_x):
        self.x = new_x

    def add_and_evaluate_y(self, y_vector):
        self.y = y_vector
        return zdt3_utils.zdt3(y_vector)

    def get_neighbors_of_individual(self, population):
        neighbors_res = []
        for neighbor_candidate in population:
            if neighbor_candidate.lambda_vector in self.neighbors:
                neighbors_res.append(neighbor_candidate)
        return neighbors_res

    def compare_with_vector(self, vector, z):
        new_f = zdt3_utils.zdt3(vector)

        # if new_f[0] <= z[0]:
        #     z[0] = new_f[0].copy()
        # if new_f[1] <= z[1]:
        #     z[1] = new_f[1].copy()

        new_g = compute_g(new_f, self.lambda_vector, z)
        old_f = zdt3_utils.zdt3(self.x)
        old_g = compute_g(old_f, self.lambda_vector, z)
        # Update x (and derives) if g<self.gx
        if new_g <= old_g:      # TODO: is <=, not <
            self.update_x(vector)

    def __str__(self):
        r = 'x: {} \n' \
            'f: {} \n' \
            'lambda: {}'.format(self.x, zdt3_utils.zdt3(self.x), self.lambda_vector)
        return r


def compute_g(f, lambdas, z):
    g_1 = lambdas[0] * abs(f[0] - z[0])
    g_2 = lambdas[1] * abs(f[1] - z[1])
    # print(type(g_1))
    return max(g_1, g_2)


def check_lower_and_upper_limit(vector):
    for i in range(vector.shape[0]):
        if vector[i] < 0.0:
            vector[i] = 0.0
        if vector[i] > 1.0:
            vector[i] = 1.0


def mutate_with_gaussian_distribution(vector_to_mutate, sigma, PR):

    # Only x_1
    random_value = random.random()
    if random_value <= PR:
        vector_to_mutate[0] = vector_to_mutate[0] + np.random.normal(0.0, sigma)

    # All the values of x
    for i in range(vector_to_mutate.shape[0]):
        random_value = random.random()
        if random_value <= PR:
            vector_to_mutate[i] = vector_to_mutate[i] + np.random.normal(0.0, sigma)
    check_lower_and_upper_limit(vector_to_mutate)
