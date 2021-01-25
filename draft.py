import numpy as np
import zdt3
import matplotlib.pyplot as plt
from random import random

# x = np.array([
# 	8.398878e-01,	3.404545e-04,	3.871110e-03,	3.672765e-02,	1.625110e-01,	3.652249e-03, 	1.181743e-03,	7.603230e-02,
#     4.621877e-02,	7.209626e-04,	1.400089e-02,	1.277078e-02,	1.156738e-02,	8.164077e-02,	3.138412e-03,	3.628732e-02,
#     9.422654e-03,	1.047997e-02,	7.592463e-03,	1.919450e-02,	4.522875e-02,	1.975934e-02,	2.672293e-02,	3.393591e-02,
#     6.233903e-02,	1.130479e-03,	3.772626e-03,	3.151231e-03,	6.845470e-02,	3.228832e-03
# ])
#
# fx = zdt3.zdt3(x)
# print(fx)

point1 = [0.0, 0.0]
point2 = [1.0, 0.0]
x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]

plt.plot(x_values, y_values)
plt.show()
# for i in range(30):
#     value = random()
#     if value <= (1.0/30.0):
#         print(value)

# print(1.0/30.)
# for i in range(3):
#     for j in range(3):
#         print('({},{})'.format(i, j))