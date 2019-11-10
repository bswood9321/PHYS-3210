# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:01:07 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt


q=.0483
E=15
K=q*E
V0=-83
x=-100
dx=1e-3
X=[x]
PSI=[np.exp(-K*np.abs(x))]
dpsi=-(np.sign(x))*K*np.exp(-K*np.abs(x))
psi=np.exp(-K*np.abs(x))
a=2

while x <=100:
    if np.abs(x)>a:
        V=0
    else:
        V=V0
        
    d2psi=(q*V+K**2)*np.exp(-K*np.abs(x))
    dpsi=dpsi+d2psi*dx
    psi=dpsi+dpsi*dx
    
    PSI.append(psi)
    x=x+dx
    X.append(x)
    
plt.plot(X,PSI)
plt.show()
    
    
    
    
