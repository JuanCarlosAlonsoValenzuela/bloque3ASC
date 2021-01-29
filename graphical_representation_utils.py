import pandas as pd
import numpy as np

def get_nsgaii(csv_path):
    df = pd.read_csv(csv_path, sep='\t', header=None)
    x = df[0].to_numpy()
    y = df[1].to_numpy()
    return np.array([x, y])