import math
import numpy as np
import pandas as pd

# generate x
def zdt3(x, n):
    out = np.zeros((2,1))
    out[0] = x[0]

    tmp = 0.0
    for i in range(1, n):
        tmp = tmp + x[i]

    # print(tmp)

    g = 1.0 + ((9.0*tmp)/(n-1.0))
    h = 1.0 - math.sqrt(out[0]/g) - (out[0]/g) * math.sin(10*math.pi*out[0])
    f_2 = g*h

    out[1] = f_2

    return out


# get pareto front
def get_pf(dat):
    df = pd.read_csv(dat, sep='\t', header=None)
    return df[0].to_numpy(), df[1].to_numpy()
