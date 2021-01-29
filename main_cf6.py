import numpy as np
import cf6_utils
import math
import cf6_utils

dat = 'PF/PF_cf6.dat'


# Get Pareto Front
pf_x, pf_y = cf6_utils.get_pf(dat)

# plt.scatter(pf_x, pf_y, s=0.8, color='red')
# plt.show()


# Recibe una x y devuelve el resultado y las restricciones

x = np.array([3.307646e-04,	8.047906e-03,	2.621420e-02,	8.173679e-02,	-1.962023e-03,	2.089632e-02,	3.748047e-02,	1.954840e-02,	6.601718e-03,	2.614146e-02,	-8.654628e-02,	1.739586e-01,	3.176427e-02,	6.292900e-02,	-2.243408e-02,	-7.862677e-02])



# TODO: Declarar valores mínimos y máximos
n = x.shape[0]

out, constr = cf6_utils.cf6(x)

print(out)
print(constr)