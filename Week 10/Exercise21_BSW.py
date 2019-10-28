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


i=0
checkpk=[]
checke=[]
while i<=1500:
    a=P[i]+K[i]
    checkpk.append(a)
    checke.append(E[i])
    i=i+1
plt.plot(checkpk,checke)
plt.show()    


#A=v0
#B=x0
#T1=np.linspace(0,15,1500)
#xt= (A*np.sin(T1*np.sqrt(k/m)))+(B*np.cos(T1*np.sqrt(k/m)))

#plt.plot(T1,xt)
#plt.show()

#xt1 = lambda T1: A*np.sin(T1*np.sqrt(k/m))+B*np.cos(T1*np.sqrt(k/m))

