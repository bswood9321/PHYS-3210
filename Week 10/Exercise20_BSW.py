# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:59:34 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

k=5
m=5
dt=.01
t=0
x=0
v=1
p=2
T=[t]
X=[x]
V=[v]

while t<=15:
    f=-k*x**(p-1)
    v=v+(f/m)*dt
    kx=(v+(f/m)*dt/2)*dt
    kv=-(k/m)*(x+v*(dt/2))*dt   
    v=v+kv
    x=x+kx
    T.append(t)
    X.append(x)
    V.append(v)
    t=t+dt
plt.plot(T,X,label='position')
plt.plot(T,V,label='velo')
plt.legend(loc=(1.04,0))
plt.grid()
plt.show()    
    