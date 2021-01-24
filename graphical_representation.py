import pandas as pd
import matplotlib.pyplot as plt
import zdt3
import numpy as np

# Paths
dat = 'PF.dat'
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

axs[0, 0].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[0])
axs[0, 0].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[0, 0].set_title('Seed 1')

axs[0, 1].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[1])
axs[0, 1].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[0, 1].set_title('Seed 2')

axs[0, 2].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[2])
axs[0, 2].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[0, 2].set_title('Seed 3')

############################################

axs[1, 0].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[3])
axs[1, 0].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[1, 0].set_title('Seed 4')

axs[1, 1].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[4])
axs[1, 1].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[1, 1].set_title('Seed 5')

axs[1, 2].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[5])
axs[1, 2].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[1, 2].set_title('Seed 6')

############################################

axs[2, 0].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[6])
axs[2, 0].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[2, 0].set_title('Seed 7')

axs[2, 1].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[7])
axs[2, 1].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[2, 1].set_title('Seed 8')

axs[2, 2].scatter(pf_x, pf_y, color='r', s=point_size)
nsgaii = get_nsgaii(paths[8])
axs[2, 2].scatter(nsgaii[0], nsgaii[1], color='b', s=point_size)
axs[2, 2].set_title('Seed 9')

for ax in fig.get_axes():
    ax.label_outer()

plt.show()