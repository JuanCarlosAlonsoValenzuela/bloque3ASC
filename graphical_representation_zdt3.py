import pandas as pd
import matplotlib.pyplot as plt
import zdt3_utils
import numpy as np
import graphical_representation_utils


# Paths
dat = 'PF/PF_zdt3.dat'
paths_nsgaii = [
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed01.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed02.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed03.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed04.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed05.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed06.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed07.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed08.out',
    'zdt3_nsgaii_results/4000/P40G100/zdt3_final_popp40g100_seed09.out'
         ]

paths_de = [
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed1.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed2.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed3.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed4.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed5.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed6.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed7.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed8.out',
    'zdt3_de_results/4000/P40G100/zdt3_final_popp40g100_seed9.out'
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
pf_x, pf_y = zdt3_utils.get_pf(dat)

fig, axs = plt.subplots(3, 3)
fig.suptitle('Comparison')

point_size = 0.3

k = 0
for i in range(3):
    for j in range(3):
        axs[i, j].scatter(pf_x, pf_y, color='r', s=point_size)
        nsgaii = graphical_representation_utils.get_nsgaii(paths_nsgaii[k])
        de = graphical_representation_utils.get_nsgaii(paths_de[k])
        axs[i, j].plot(nsgaii[0], nsgaii[1], '.', color='b')
        axs[i, j].plot(de[0], de[1], '.',color='g')
        axs[i, j].set_title('Seed {}'.format(k+1))
        axs[i, j].set_ylim([-0.8, 1.3])
        k = k + 1

for ax in fig.get_axes():
    ax.label_outer()

plt.show()