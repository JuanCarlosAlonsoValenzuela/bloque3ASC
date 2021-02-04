import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

N = 200
G = 50
path = 'tmp_zdt3p{}g{}/spacing{}.out'


for i in range(1, 11):
    df = pd.read_csv(path.format(N, G, i), header=None, sep='\t')
    array = df[1].to_numpy()
    plt.plot(array, '-', color='b', linewidth=1)


for j in range(11, 21):
    df = pd.read_csv(path.format(N, G, j), header=None, sep='\t')
    array = df[1].to_numpy()
    plt.plot(array, '-', color='r', linewidth=1)

red_patch = mpatches.Patch(color='red', label='nsgaii')
blue_patch = mpatches.Patch(color='blue', label='de')

plt.title("Spacing with N={} and G={}".format(N, G))
plt.legend(handles=[red_patch, blue_patch])
plt.show()


# for i in range(1, 11):
    # print(i)
