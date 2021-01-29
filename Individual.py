import numpy as np
import random
import zdt3_utils
import cf6_utils


class Individual:
    def __init__(self, n, lambda_vector, t_neighbors):

        x = np.zeros((n,))
        for j in range(n):
            element = random.random()
            x[j] = element

        self.x = x                          # Individual of n dimensions (genotype)
        self.lambda_vector = lambda_vector  # lambda
        self.neighbors = t_neighbors        # B
        self.y = np.zeros((n,))

    def update_x(self, new_x):
        self.x = new_x

    def add_and_evaluate_y_zdt3(self, y_vector):
        self.y = y_vector
        return zdt3_utils.zdt3(y_vector)

    def add_and_evaluate_y_cf6(self, y_vector):
        self.y = y_vector
        return cf6_utils.cf6(y_vector)

    def get_neighbors_of_individual(self, population):
        neighbors_res = []
        for neighbor_candidate in population:
            if neighbor_candidate.lambda_vector in self.neighbors:
                neighbors_res.append(neighbor_candidate)
        return neighbors_res

    def compare_with_vector_zdt3(self, vector, z):
        new_f = zdt3_utils.zdt3(vector)
        new_g = compute_g(new_f, self.lambda_vector, z)

        old_f = zdt3_utils.zdt3(self.x)
        old_g = compute_g(old_f, self.lambda_vector, z)

        # Update x (and derives) if new_g <= old_g
        if new_g <= old_g:
            self.update_x(vector)

    def compare_with_vector_cf6(self, vector, z):
        new_f, constr_new_f = cf6_utils.cf6(vector)
        new_g = compute_g(new_f, self.lambda_vector, z)

        old_f, constr_old_f = cf6_utils.cf6(self.x)
        old_g = compute_g(old_f, self.lambda_vector, z)

        # A constraint is violated if its value is beneath zero
        old_feasible = (constr_old_f[0] >= 0.0) and (constr_old_f[1] >= 0.0)
        new_feasible = (constr_new_f[0] >= 0.0) and (constr_new_f[1] >= 0.0)

        # If both are feasible
        if new_feasible and old_feasible:
            if new_g <= old_g:      # Select the one with the greatest fitness
                self.update_x(vector)

        # If only one is feasible (This operation is equivalent to xor)
        elif new_feasible != old_feasible:
            if new_feasible:
                self.update_x(vector)

        # If none of the individuals is feasible, select the one that violates less restrictions
        else:
            old_sum = 0.0
            new_sum = 0.0

            if constr_old_f[0] < 0.0:
                old_sum = old_sum + abs(constr_old_f[0])
            if constr_old_f[1] < 0.0:
                old_sum = old_sum + abs(constr_old_f[1])

            if constr_new_f[0] < 0.0:
                new_sum = new_sum + abs(constr_new_f[0])
            if constr_new_f[1] < 0.0:
                new_sum = new_sum + abs(constr_new_f[1])

            if new_sum >= old_sum:
                self.update_x(vector)




    def __str__(self):
        r = 'x: {} \n' \
            'f: {} \n' \
            'lambda: {}'.format(self.x, zdt3_utils.zdt3(self.x), self.lambda_vector)
        return r


def compute_g(f, lambdas, z):
    g_1 = lambdas[0] * abs(f[0] - z[0])
    g_2 = lambdas[1] * abs(f[1] - z[1])
    return max(g_1, g_2)


def check_lower_and_upper_limit_zdt3(vector):
    for i in range(vector.shape[0]):
        if vector[i] < 0.0:
            vector[i] = 0.0
        if vector[i] > 1.0:
            vector[i] = 1.0


def check_lower_and_upper_limit_cf6(vector):
    # Limits
    # i = 0 -->     min= 0.0,   max=1.0
    # i > 0 -->     min= -2.0,  max=2.0
    # Check limit of x[0]
    if vector[0] < 0.0:
        vector[0] = 0.0
    if vector[0] > 1.0:
        vector[0] = 1.0

        # Check limit of the rest of elements
    for i in range(1, vector.shape[0]):
        if vector[i] > 2.0:
            vector[i] = 2.0
        if vector[i] < -2.0:
            vector[i] = -2.0


def mutate_with_gaussian_distribution_zdt3(vector_to_mutate, sigma, PR):

    # Only x_1
    random_value = random.random()
    if random_value <= PR:
        vector_to_mutate[0] = vector_to_mutate[0] + np.random.normal(0.0, sigma)

    # All the values of x
    for i in range(vector_to_mutate.shape[0]):
        random_value = random.random()
        if random_value <= PR:
            vector_to_mutate[i] = vector_to_mutate[i] + np.random.normal(0.0, sigma)
    check_lower_and_upper_limit_zdt3(vector_to_mutate)


def mutate_with_gaussian_distribution_cf6(vector_to_mutate, sigma, PR):

    # Only x_1
    # random_value = random.random()
    # if random_value <= PR:
    #     vector_to_mutate[0] = vector_to_mutate[0] + np.random.normal(0.0, sigma)

    # All the values of x
    for i in range(vector_to_mutate.shape[0]):
        random_value = random.random()
        if random_value <= PR:
            vector_to_mutate[i] = vector_to_mutate[i] + np.random.normal(0.0, sigma)
    check_lower_and_upper_limit_cf6(vector_to_mutate)
