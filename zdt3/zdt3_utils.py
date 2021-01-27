import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# generate x
def zdt3(x):
    n = x.shape[0]      # Derivate n (30)
    out = np.zeros(2)
    out[0] = x[0]

    tmp = 0.0
    for i in range(1, n):
        tmp = tmp + x[i]

    g = 1.0 + ((9.0*tmp)/(n-1.0))
    h = 1.0 - math.sqrt(out[0]/g) - (out[0]/g) * math.sin(10*math.pi*out[0])
    f_2 = g*h

    out[1] = f_2

    return out


# get pareto front
def get_pf(dat):
    df = pd.read_csv(dat, sep='\t', header=None)
    return df[0].to_numpy(), df[1].to_numpy()


# return representation of a population8
def get_representation(population, N):
    f_1 = np.zeros([N, 1])  # F1 (phenotype)
    f_2 = np.zeros([N, 1])  # F2 (phenotype)
    for i in range(N):
        individual = population[i]
        fx = zdt3(individual.x)
        f_1[i] = fx[0]
        f_2[i] = fx[1]

    return f_1, f_2


def get_representation_of_weights(individual, z):
    point1 = z # [0.0, 0.0]
    x_values = [point1[0], individual.lambda_vector[0] + point1[0]]
    y_values = [point1[1], individual.lambda_vector[1] + point1[1]]

    # Print lambda
    plt.plot(x_values, y_values, color='b', linewidth = 1)
    # plt.xlim([0.0, 6.0])
    # plt.ylim([0.0, 6.0])

    for neighbor in individual.neighbors:
        if neighbor[0] != individual.lambda_vector[0] and neighbor[1] != individual.lambda_vector[1]:
            x_values = [point1[0], neighbor[0] + point1[0]]
            y_values = [point1[1], neighbor[1] + point1[1]]
            plt.plot(x_values, y_values, color='g', linewidth = 1)

    # plt.show()


def get_representation_of_all_weights(population):
    point1 = [0.0, 0.0]
    for individual in population:
        x_values = [point1[0], 6*individual.lambda_vector[0]]
        y_values = [point1[1], 6*individual.lambda_vector[1]]

        # Print lambda
        plt.plot(x_values, y_values, color='b')
        plt.xlim([0.0, 6.0])
        plt.ylim([0.0, 6.0])

        for neighbor in individual.neighbors:
            if neighbor[0] != individual.lambda_vector[0] and neighbor[1] != individual.lambda_vector[1]:
                x_values = [point1[0], 6*neighbor[0]]
                y_values = [point1[1], 6*neighbor[1]]
                plt.plot(x_values, y_values, color='r')

        plt.show()
