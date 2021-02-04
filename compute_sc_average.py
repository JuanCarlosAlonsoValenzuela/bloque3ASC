import pandas as pd
import numpy as np

N = 40
G = 100

path1 = 'tmp_zdt3p{}g{}/cs1_{}.out'
path2 = 'tmp_zdt3p{}g{}/cs2_{}.out'

acum = np.zeros(10)
j = 1
while j <= 10:
    if j == 10:
        df = pd.read_csv(path2.format(N, G, 99), header=None, sep='\t')
    else:
        df = pd.read_csv(path2.format(N, G, j), header=None, sep='\t')
    array = df[1].to_numpy()
    value = array[len(array)-1]
    acum[j-1] = value
    j = j + 1

average = np.mean(acum)
dev = np.std(acum)
print('Average: {}'.format(average))
print('std: {}'.format(dev))
print('---------------------')


acum = np.zeros(10)
i = 1
while i <= 10:
    if i == 10:
        df = pd.read_csv(path1.format(N, G, 99), header=None, sep='\t')
    else:
        df = pd.read_csv(path1.format(N, G, i), header=None, sep='\t')
    array = df[1].to_numpy()
    value = array[len(array)-1]
    acum[i-1] = value
    i = i + 1

average = np.mean(acum)
dev = np.std(acum)
print('Average: {}'.format(average))
print('std: {}'.format(dev))
print('---------------------')