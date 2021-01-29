import numpy as np
import pandas as pd
import math


# get pareto front
def get_pf(dat):
    df = pd.read_csv(dat, sep='\t', header=None)
    return df[0].to_numpy(), df[1].to_numpy()


# Sign function
def sgn(sgn_input):
    if sgn_input > 0.0:
        return 1.0
    else:
        return -1.0


# Compute cf6 and check limits
def cf6(x):
    n = x.shape[0]

    # Limits
    # i = 0 -->     min= 0.0,   max=1.0
    # i > 0 -->     min= -2.0,  max=2.0
    # Check limit of x[0]
    if x[0] < 0.0:
        x[0] = 0.0
    if x[0] > 1.0:
        x[0] = 1.0

    # Check limit of the rest of elements
    for i in range(1,n):
        if x[i] > 2.0:
            x[i] = 2.0
        if x[i] < -2.0:
            x[i] = -2.0

    # Initialize out
    out = np.zeros([2])
    constr = np.zeros([2])

    # Initialize sum
    sum1 = np.zeros([1])
    sum2 = np.zeros([1])

    for j in range(2, n + 1):
        if j % 2 == 1:
            yj = x[j-1] - 0.8*x[0]*math.cos(6.0*math.pi*x[0] + (j*math.pi)/n)
            sum1 = sum1 + math.pow(yj, 2)
        else:
            yj = x[j-1] - 0.8*x[0]*math.sin(6.0*math.pi*x[0] + (j*math.pi)/n)
            sum2 = sum2 + math.pow(yj, 2)

    # Compute out
    out[0] = x[0] + sum1
    out[1] = pow(1.0 - x[0], 2) + sum2

    # Compute restrictions
    constr[0] = x[1] - 0.8*x[0]*math.sin(6.0*x[0]*math.pi+2.0*math.pi/n) - sgn((x[0]-0.5)*(1.0-x[0]))*math.sqrt(abs((x[0]-0.5)*(1.0-x[0])))
    constr[1] = x[3] - 0.8*x[0]*math.sin(6.0*x[0]*math.pi+4.0*math.pi/n) - sgn(0.25*math.sqrt(1.0-x[0]) - 0.5*(1.0-x[0]))*math.sqrt(abs(0.25*math.sqrt(1.0-x[0])-0.5*(1.0-x[0])))

    return out, constr


def get_representation(population, N):
    f_1 = np.zeros([N, 1])  # F1 (phenotype)
    f_2 = np.zeros([N, 1])  # F2 (phenotype)
    for i in range(N):
        individual = population[i]
        fx, constrx = cf6(individual.x)
        f_1[i] = fx[0]
        f_2[i] = fx[1]

    return f_1, f_2