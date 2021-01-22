import math
import numpy as np
import pandas as pd


# generate x
def zdt3(x):
    n = x.shape[0]      # Derivate n (30)
    out = np.zeros((2, 1))
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
        f_1[i] = individual.fx[0]
        f_2[i] = individual.fx[1]

    return f_1, f_2
