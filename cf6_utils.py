import numpy as np
import pandas as pd


# get pareto front
def get_pf(dat):
    df = pd.read_csv(dat, sep='\t', header=None)
    return df[0].to_numpy(), df[1].to_numpy()


