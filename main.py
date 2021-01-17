import numpy as np
import math
import matplotlib.pyplot as plt
from random import random
from random import seed
import zdt3

# HYPERPARAMETERS:
N = 100         # Population size
T = 30          # Neighborhood size
G = 40          # Number of generations

# Seed random number generator
# seed(1)
# n = 30
# f_1 = []
# f_3 = []
# for i in range(100):
#     w = []
#     for j in range(n):
#         element = random()
#         w.append(round(random(), 3))
#
#     out2 = zdt3.zdt3(w, n)
#     f_1.append(out2[0])
#     f_3.append(out2[1])
#
# print(f_1)
# print(f_3)
# plt.plot(f_1, f_3, '.')
# plt.show()
