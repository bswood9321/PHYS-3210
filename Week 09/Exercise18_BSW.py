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
errors=np.sqrt(decays)+2
data=np.column_stack((data,errors))

plt.errorbar(time,decays,yerr=errors)
plt.title("Pi meson decays")
plt.show()




def f(t,N0,T):
    return N0*np.exp(-t/T)

y = f(time,10000,2.6e-8)

popt,pcov=op.curve_fit(f,time,decays)

plt.plot(time,f(time,*popt))
plt.errorbar(time,decays,yerr=errors)
plt.xlabel('time')
plt.ylabel('decays')
plt.show()