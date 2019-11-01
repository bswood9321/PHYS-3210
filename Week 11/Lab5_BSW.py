# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:04:56 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

k=10
m=1
g=9.8
dt=.001
t=0
x0=1
v0=0
p=2
N=m*g
mus=0.1
muk=0.1
w0=np.sqrt(k/m)
b_u=(2*m*w0)-5
b_c=(2*m*w0)
b_o=(2*m*w0)+5
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
    Fs=-mus*N
    Fk=-muk*N*(v/np.absolute(v))
    Fv=-(b_u)*v
    if v==0:
        Fk=0
    else:
        Fs=0
    f=(-k*x**(p-1))+Fs+Fk+Fv
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
plt.title("Underdamped Spring")
plt.grid()
plt.show()

plt.plot(T,K,label='Kinetic Energy')
plt.plot(T,P,label='Potential E')
plt.plot(T,E,label='Total E')
plt.legend(loc=(1.04,0))
plt.title("Underdamped Spring Energy Graph")
plt.show()

plt.plot(T,S,label='Stability')
plt.legend()
plt.title("Underdamped Spring Stability Graph")
plt.show()

KEave=np.sum(K)/len(K)
PEave=np.sum(P)/len(P)

print('Time average of Kinetic Energy= ',KEave) 
print('Time average of Potential Energy= ',PEave)

g=9.8
dt=.001
t=0
N=m*g
mus=0.1
muk=0.1
w0=np.sqrt(k/m)
b_u=(2*m*w0)-5
b_c=(2*m*w0)
b_o=(2*m*w0)+5
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
    Fs=-mus*N
    Fk=-muk*N*(v/np.absolute(v))
    Fv=-(b_c)*v
    if v==0:
        Fk=0
    else:
        Fs=0
    f=(-k*x**(p-1))+Fs+Fk+Fv
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
plt.title("Critically Damped Spring")
plt.grid()
plt.show()

plt.plot(T,K,label='Kinetic Energy')
plt.plot(T,P,label='Potential E')
plt.plot(T,E,label='Total E')
plt.legend(loc=(1.04,0))
plt.title("Critically Damped Spring Energy Graph")
plt.show()

plt.plot(T,S,label='Stability')
plt.legend()
plt.title("Critically Damped Spring Stability Graph")
plt.show()

KEave=np.sum(K)/len(K)
PEave=np.sum(P)/len(P)

print('Time average of Kinetic Energy= ',KEave) 
print('Time average of Potential Energy= ',PEave)

g=9.8
dt=.001
t=0
N=m*g
mus=0.1
muk=0.1
w0=np.sqrt(k/m)
b_u=(2*m*w0)-5
b_c=(2*m*w0)
b_o=(2*m*w0)+5
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
    Fs=-mus*N
    Fk=-muk*N*(v/np.absolute(v))
    Fv=-(b_o)*v
    if v==0:
        Fk=0
    else:
        Fs=0
    f=(-k*x**(p-1))+Fs+Fk+Fv
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
plt.title("Overdamped Spring")
plt.grid()
plt.show()

plt.plot(T,K,label='Kinetic Energy')
plt.plot(T,P,label='Potential E')
plt.plot(T,E,label='Total E')
plt.legend(loc=(1.04,0))
plt.title("Overdamped Spring Energy Graph")
plt.show()

plt.plot(T,S,label='Stability')
plt.legend()
plt.title("Overdamped Spring Stability Graph")
plt.show()

KEave=np.sum(K)/len(K)
PEave=np.sum(P)/len(P)

print('Time average of Kinetic Energy= ',KEave) 
print('Time average of Potential Energy= ',PEave)

g=9.8
dt=.001
t=0
N=m*g
mus=0.1
muk=0.1
w0=np.sqrt(k/m)
b_u=(2*m*w0)-5
b_c=(2*m*w0)
b_o=(2*m*w0)+5
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
    Fs=-mus*N
    Fk=-muk*N*(v/np.absolute(v))
    Fv=-b_o
    if v==0:
        Fk=0
    else:
        Fs=0
    f=(-k*x**(p-1))+Fk+Fs
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
plt.title("No damping Spring")
plt.grid()
plt.show()

plt.plot(T,K,label='Kinetic Energy')
plt.plot(T,P,label='Potential E')
plt.plot(T,E,label='Total E')
plt.legend(loc=(1.04,0))
plt.title("No damping Spring Energy Graph")
plt.show()

plt.plot(T,S,label='Stability')
plt.legend()
plt.title("No damping Spring Stability Graph")
plt.show()

KEave=np.sum(K)/len(K)
PEave=np.sum(P)/len(P)

print('Time average of Kinetic Energy= ',KEave) 
print('Time average of Potential Energy= ',PEave)