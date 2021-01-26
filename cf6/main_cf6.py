import numpy as np
import matplotlib.pyplot as plt
import cf6.cf6_utils as cf6

dat = 'PF_cf6.dat'

# Get Pareto Front
pf_x, pf_y = cf6.get_pf(dat)


plt.scatter(pf_x, pf_y, s=0.8, color='red')
plt.show()
