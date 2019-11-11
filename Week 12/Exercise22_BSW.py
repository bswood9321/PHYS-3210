# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:01:07 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt


q=.0483
E=-10
K=q*E
V0=-83
x=-100
dx=1e-3
X=[x]
PSI=[np.exp(K*np.abs(x))]
dpsi=-(np.sign(x))*K*np.exp(K*np.abs(x))
psi=np.exp(K*np.abs(x))
a=2

while x <=a:
    if np.abs(x)>a:
        V=0
    else:
        V=V0
        
    d2psi=(q*V+K**2)*np.exp(K*np.abs(x))
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    
    PSI.append(psi)
    x=x+dx
    X.append(x)
    
x1=100
X1=[x1] 
PSI1=[np.exp(K*np.abs(x))]
dpsi1=-(np.sign(x))*K*np.exp(K*np.abs(x))
psi1=np.exp(K*np.abs(x))   

while x1 >=a:
    if np.abs(x1)>a:
        V=0
    else:
        V=V0
        
    d2psi1=(q*V+K**2)*np.exp(K*np.abs(x1))
    dpsi1=dpsi1+d2psi1*dx
    psi1=psi1+dpsi1*dx
    
    PSI1.append(psi1)
    x1=x1-dx
    X1.append(x1)   
    
    
plt.plot(X,PSI)
plt.plot(X1,PSI1)
plt.xlim(-5,5)

plt.show()
    
    
    
    
