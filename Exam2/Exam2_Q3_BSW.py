# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:49:01 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

theta=np.pi/8
w=0
l=2
g=9.82
t=0
m=5
dt=.01
THETA=[theta]
W=[w]
T=[t]
X=[l*np.sin(theta)]
Y=[l-l*np.cos(theta)]
findT=[]
while t<=10:
    x=l*np.sin(theta)
    y=l-l*np.cos(theta)
    f=-m*g*np.sin(theta)
    w=w+(f/m)*dt
    theta = theta+w*dt
    t=t+dt
    T.append(t)
    X.append(x)
    Y.append(y)
    THETA.append(theta)
    W.append(w)


plt.plot(T,X,label='x')
plt.plot(T,W,label='w')
plt.plot(T,THETA,label='angle')
plt.plot(T,Y,label='y')
plt.legend(loc=(1.04,0))
plt.show()

plt.plot(X,Y)
plt.show()

plt.plot(THETA,W)
plt.show()

print('The theoretical Tau is: ',2*np.pi*np.sqrt((l/g)))