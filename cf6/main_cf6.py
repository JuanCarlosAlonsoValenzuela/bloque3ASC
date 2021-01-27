import numpy as np
import matplotlib.pyplot as plt
import cf6.cf6_utils as cf6
import math

dat = 'PF_cf6.dat'

# Get Pareto Front
pf_x, pf_y = cf6.get_pf(dat)

# plt.scatter(pf_x, pf_y, s=0.8, color='red')
# plt.show()


# Recibe una x y devuelve el resultado y las restricciones

x = np.array([1.220245e-08, 1.434681e-05, 2.153731e-04, -5.203644e-02])
# x = np.array([5.758273e-01,	1.161506e-01,	3.459767e-01,	4.545745e-01])

# TODO: Declarar valores mínimos y máximos

# i = 0 -->     min= 0.0,   max=1.0
# i > 0 -->     min= -2.0,  max=2.0
n = x.shape[0]
# Initialize out
out = np.zeros([2])

# Initialize sum
sum1 = np.zeros([1])
sum2 = np.zeros([1])

for j in range(2, n):
    if j % 2 == 1:
        yj = x[j-1] - 0.8*x[0]*math.cos(6.0*math.pi*x[0] + (j*math.pi)/n)
        sum1 = sum1 + math.pow(yj, 2)
    else:
        yj = x[j-1] - 0.8*x[0]*math.sin(6.0*math.pi*x[0] + (j*math.pi)/n)
        sum2 = sum2 + math.pow(yj, 2)

# Compute out
out[0] = x[0] + sum1
out[1] = pow(1.0 - x[0], 2) + sum2

# Compute restrictions

print(out)
