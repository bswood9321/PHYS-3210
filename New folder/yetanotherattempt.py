# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:48:52 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

n=1
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
X=[x]
PSI=[0]
P=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    X.append(x)
    PSI.append(psi)
    P.append((np.sqrt(2/L)*np.sin(k*x))**2)


n=2
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
PSI2=[0]
P2=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    PSI2.append(psi+5)
    P2.append(((np.sqrt(2/L)*np.sin(k*x))**2)+5)
    
n=3
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
PSI3=[0]
P3=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    PSI3.append(psi+10)
    P3.append(((np.sqrt(2/L)*np.sin(k*x))**2)+10)

n=4
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
PSI4=[0]
P4=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    PSI4.append(psi+15)
    P4.append(((np.sqrt(2/L)*np.sin(k*x))**2)+15)    
    
xgrid=[0,1]
ygrid=[[0,0],[5,5],[10,10],[15,15]]

plt.figure(figsize=(3,6))
plt.plot(X,PSI)
plt.plot(xgrid,ygrid[0],color='black')
plt.plot(xgrid,ygrid[1],color='black')
plt.plot(xgrid,ygrid[2],color='black')
plt.plot(xgrid,ygrid[3],color='black')
plt.plot(X,PSI2)
plt.plot(X,PSI3)
plt.plot(X,PSI4)
plt.xlim(0,1)
plt.yticks([0,5,10,15],('n=1','n=2','n=3','n=4'))
plt.xticks([0,1],('0','L'))
plt.show()    
    
plt.figure(figsize=(3,6))
plt.plot(X,P)
plt.plot(X,P2)
plt.plot(X,P3)
plt.plot(X,P4)
plt.plot(xgrid,ygrid[0],color='black')
plt.plot(xgrid,ygrid[1],color='black')
plt.plot(xgrid,ygrid[2],color='black')
plt.plot(xgrid,ygrid[3],color='black')
plt.xlim(0.1,1)
plt.yticks([0,5,10,15],('n=1','n=2','n=3','n=4'))
plt.xticks([0,1],('0','L'))
plt.show()