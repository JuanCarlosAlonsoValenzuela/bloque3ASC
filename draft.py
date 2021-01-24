import numpy as np
import zdt3
import matplotlib.pyplot as plt

# x = np.array([
# 	8.398878e-01,	3.404545e-04,	3.871110e-03,	3.672765e-02,	1.625110e-01,	3.652249e-03, 	1.181743e-03,	7.603230e-02,
#     4.621877e-02,	7.209626e-04,	1.400089e-02,	1.277078e-02,	1.156738e-02,	8.164077e-02,	3.138412e-03,	3.628732e-02,
#     9.422654e-03,	1.047997e-02,	7.592463e-03,	1.919450e-02,	4.522875e-02,	1.975934e-02,	2.672293e-02,	3.393591e-02,
#     6.233903e-02,	1.130479e-03,	3.772626e-03,	3.151231e-03,	6.845470e-02,	3.228832e-03
# ])
#
# fx = zdt3.zdt3(x)
# print(fx)




# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0,0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0,1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1,0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1,1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()