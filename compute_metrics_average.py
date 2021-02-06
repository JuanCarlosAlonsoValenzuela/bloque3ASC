import pandas as pd
import numpy as np


N = 40
G = 100
d = 4

path = 'tmp_cf6_{}dp{}g{}/spacing{}.out'

# 1.- Leer última fila de cada archivo
acum = np.zeros(10)
for i in range(1, 11):
    df = pd.read_csv(path.format(d, N, G, i), header=None, sep='\t')

    array = df[1].to_numpy()
    value = array[len(array)-1]

    acum[i-1] = value

average = np.mean(acum)
dev = np.std(acum)
print('average: {}'.format(average))
print('std: {}'.format(dev))
print('---------------------')
# 2.- Calcular media y desviación típica

acum = np.zeros(10)
for j in range(11, 21):
    df = pd.read_csv(path.format(d, N, G, j), header=None, sep='\t')

    array = df[1].to_numpy()
    value = array[len(array)-1]

    acum[j-11] = value


average = np.mean(acum)
dev = np.std(acum)
print('average: {}'.format(average))
print('std: {}'.format(dev))
