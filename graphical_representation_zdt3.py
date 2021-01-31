import pandas as pd
import matplotlib.pyplot as plt
import zdt3_utils
import numpy as np
import graphical_representation_utils

N = 200
G = 50
n_eval = N*G


# Paths
dat = 'PF/PF_zdt3.dat'

paths_nsgaii = []
paths_de = []

for i in range(1, 10):
    new_path_nsgaii = 'zdt3_nsgaii_results/{}/P{}G{}/zdt3_final_popp{}g{}_seed0{}.out'.format(n_eval, N, G, N, G, i)
    paths_nsgaii.append(new_path_nsgaii)

    new_path_de = 'zdt3_de_results/{}/P{}G{}/zdt3_final_popp{}g{}_seed{}.out'.format(n_eval, N, G, N, G, i)
    paths_de.append(new_path_de)

# Get Pareto Front
pf_x, pf_y = zdt3_utils.get_pf(dat)

fig, axs = plt.subplots(3, 3)
fig.suptitle('Comparison of ZDT3 for N={} and G={} ({} EVALUATIONS)'.format(N, G, n_eval))

point_size = 0.3

k = 0
for i in range(3):
    for j in range(3):
        axs[i, j].scatter(pf_x, pf_y, color='r', s=point_size, label='PF')
        nsgaii = graphical_representation_utils.get_nsgaii(paths_nsgaii[k])
        de = graphical_representation_utils.get_nsgaii(paths_de[k])
        axs[i, j].plot(nsgaii[0], nsgaii[1], '.', color='b', label='NSGAII')
        axs[i, j].plot(de[0], de[1], '.',color='g', label='DE')
        axs[i, j].set_title('Seed {}'.format(k+1))
        axs[i, j].set_ylim([-0.8, 1.3])
        axs[i, j].legend()
        k = k + 1

for ax in fig.get_axes():
    ax.label_outer()

plt.show()