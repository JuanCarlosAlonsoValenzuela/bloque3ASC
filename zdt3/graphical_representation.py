import pandas as pd
import matplotlib.pyplot as plt
from zdt3 import zdt3
import numpy as np

# Paths
dat = 'PF_zdt3.dat'
paths = [
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed01.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed02.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed03.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed04.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed05.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed06.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed07.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed08.out',
    'zdt3_nsgaii/4000/P40G100/zdt3_final_popp40g100_seed09.out'
         ]

# paths = [
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed01.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed02.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed03.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed04.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed05.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed06.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed07.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed08.out',
#     'zdt3_nsgaii/10000/P200G50/zdt3_final_popp200g50_seed09.out'
#          ]


# Get Pareto Front
pf_x, pf_y = zdt3.get_pf(dat)


def get_nsgaii(csv_path):
    df = pd.read_csv(csv_path, sep='\t', header=None)
    x = df[0].to_numpy()
    y = df[1].to_numpy()
    return np.array([x, y])


fig, axs = plt.subplots(3, 3)
fig.suptitle('Comparison')

point_size = 0.3

k = 0
for i in range(3):
    for j in range(3):
        axs[i, j].scatter(pf_x, pf_y, color='r', s=point_size)
        nsgaii = get_nsgaii(paths[k])
        axs[i, j].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
        axs[i, j].set_title('Seed {}'.format(k+1))
        axs[i, j].set_ylim([-0.8, 1.3])
        k = k + 1

for ax in fig.get_axes():
    ax.label_outer()

plt.show()