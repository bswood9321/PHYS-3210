# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:01:07 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

a=2
E=-15
K2=.0483*(E+V0)
x=np.arange(-100,100,1.0e-2)
Psi=[]
i=0
while i<=19999:
    if np.abs(x[i])>a:
        V0=0
    else:
        V0=-83
    psi=np.exp((K2)*np.abs(x[i]))
    Psi.append(psi)
    i+=1
    




plt.plot(x,Psi)
plt.xlim(-3,3)
plt.show()