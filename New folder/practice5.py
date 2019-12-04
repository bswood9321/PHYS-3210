# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:32:47 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

l=1
n=2
x=-l
X=np.arange(-l,l,.001)
dx=.001
psi=np.sqrt(2/l)*np.sin(n*np.pi*x/l)
dpsi=np.sqrt(2)*np.pi*n*np.cos(n*np.pi*x/l)/(l**1.5)
d2psi=np.sqrt(2)*np.pi**2*n**2*np.sin(n*np.pi*x/l)/(l**2.5)
PSI=[]
while x<=(l):
    d2psi=np.sqrt(2)*np.pi**2*n**2*np.sin(n*np.pi*x/l)/(l**2.5)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    PSI.append(psi)
    x=x+dx
plt.plot(X,PSI)
plt.show()    

psii=np.sqrt(2/l)*np.sin(n*np.pi*X/l)

plt.plot(X,psii)
plt.show()

e0=8.8541878128e-12
echarge=1.60217662e-19
hbar=1.0545718e-34
me=9.10938356e-31
a0=5.29177210903e-11
c=299792458
h=6.6260693e-34

def v(n):
    vn=hbar/(me*a0*n)
    return vn

x0=a0*np.cos(45)
y0=a0*np.sin(30)
z0=0
vx0=-1e-10
vy0=1e-10
vz0=0

m=1e-5
t=0
dt=.0001
x=x0
y=y0
z=z0
vx=vx0
vy=vy0
vz=vz0
X=[x]
Y=[y]
Z=[z]
T=[t]
Vx=[vx]
Vy=[vy]
Vz=[vz]


while t<=10:
    Fx=-echarge**2*x/((x**2+y**2+z**2)**1.5)
    Fy=-echarge**2*y/((x**2+y**2+z**2)**1.5)
    Fz=-echarge**2*z/((x**2+y**2+z**2)**1.5)
    vx=vx+Fx/m*dt
    vy=vy+Fy/m*dt
    vz=vz+Fz/m*dt
    x=x+vx*dt
    y=y+vy*dt
    z=z+vz*dt
    X.append(x)
    Y.append(y)
    Z.append(z)
    T.append(t)
    t=t+dt
    
plt.plot(X,Y)
plt.show()





