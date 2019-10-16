# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

data = np.loadtxt("pi_meson_decays.dat")
time = data[:,0]
decays=data[:,1]
errors=np.sqrt(decays)
data=np.column_stack((data,errors))

plt.errorbar(time,decays,yerr=errors)
plt.title("Pi meson decays")
plt.show()

a1=430
a2=2e-7    #guesses
g=a1+a2*time
plt.plot(time,g)