import pandas as pd
import matplotlib.pyplot as plt
import cf6_utils
import numpy as np
import graphical_representation_utils

# TODO: Change color if constraints are violated

# Paths
dat = 'PF/PF_cf6.dat'

paths = [
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed01.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed02.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed03.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed04.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed05.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed06.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed07.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed08.out',
    'cf6_4d_results/4000/P40G100/cf6_4d_final_popp40g100_seed09.out'
]

# Get Pareto Front
pf_x, pf_y = cf6_utils.get_pf(dat)

fig, axs = plt.subplots(3, 3)
fig.suptitle('Comparison')

point_size = 0.3
k = 0
for i in range(3):
    for j in range(3):
        axs[i, j].scatter(pf_x, pf_y, color='r', s=point_size)
        nsgaii = graphical_representation_utils.get_nsgaii(paths[k])
        axs[i, j].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
        axs[i, j].set_title('Seed {}'.format(k+1))
        # axs[i, j].set_ylim([-0.8, 1.3])
        k = k + 1

for ax in fig.get_axes():
    ax.label_outer()

plt.show()

