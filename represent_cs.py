import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

N = 40
G = 100
d = 4
path1 = 'tmp_cf6_{}dp{}g{}/cs1_{}.out'
path2 = 'tmp_cf6_{}dp{}g{}/cs2_{}.out'

# de
i = 1
while i <= 10:
    if i == 10:
        i = 99

    df = pd.read_csv(path1.format(d, N, G, i), header=None, sep='\t')
    array = df[1].to_numpy()
    plt.plot(array, '-', color='b', linewidth=1)
    i = i + 1

j = 1
while j <= 10:
    if j == 10:
        j = 99

    df = pd.read_csv(path2.format(d, N, G, j), header=None, sep='\t')
    array = df[1].to_numpy()
    plt.plot(array, '-', color='r', linewidth=1)
    j = j + 1

red_patch = mpatches.Patch(color='red', label='C(DE, NSGAII)')
blue_patch = mpatches.Patch(color='blue', label='C(NSGAII, DE)')

plt.title("Coverage set with d={}, N={} and G={}".format(d, N, G))
plt.legend(handles=[red_patch, blue_patch])
plt.show()