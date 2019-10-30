# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

k=10
m=1
dt=.001
t=0
x0=-3
v0=0
p=2
x=x0
v=v0
kin=(1/2)*m*(v**2)
pe=(1/2)*k*(x**2)
kin0=kin
pe0=pe
tot=kin+pe
tot0=tot
s= (np.absolute((tot-tot0)/tot0))
T=[t]
X=[x]
V=[v]
K=[kin]
P=[pe]
E=[tot]
S=[s]
while t<=15:
    f=-k*x**(p-1)
    v=v+(f/m)*dt
    kx=(v+(f/m)*dt/2)*dt
    kv=-(k/m)*(x+v*(dt/2))*dt   
    v=v+kv
    x=x+kx
    kin= (1/2)*m*(v**2)
    pe=(1/2)*k*(x**2)
    tot=kin+pe
    s=(np.absolute((tot-tot0)/tot0))
    T.append(t)
    X.append(x)
    V.append(v)
    K.append(kin)
    P.append(pe)
    E.append(tot)
    S.append(s)
    t=t+dt
plt.plot(T,X,label='position')
plt.plot(T,V,label='velo')
plt.legend(loc=(1.04,0))
plt.grid()
plt.show()

plt.plot(T,K,label='Kinetic Energy')
plt.plot(T,P,label='Potential E')
plt.plot(T,E,label='Total E')
plt.legend(loc=(1.04,0))
plt.show()

plt.plot(T,S,label='Stability')
plt.legend()
plt.show()

KEave=np.sum(K)/len(K)
PEave=np.sum(P)/len(P)

print('Time average of Kinetic Energy= ',KEave) 
print('Time average of Potential Energy= ',PEave)



