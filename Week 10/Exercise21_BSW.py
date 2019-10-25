# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

k=10
m=1
dt=.01
t=0
x0=0
v0=-1
p=2
x=x0
v=v0

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

A=v0
B=x0
T1=np.linspace(0,15,1500)
xt= (A*np.sin(T1*np.sqrt(k/m)))+(B*np.cos(T1*np.sqrt(k/m)))

plt.plot(T1,xt)
plt.show()

xt1 = lambda T1: A*np.sin(T1*np.sqrt(k/m))+B*np.cos(T1*np.sqrt(k/m))

