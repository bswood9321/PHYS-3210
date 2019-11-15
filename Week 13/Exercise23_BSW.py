# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:33:28 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

x0=0.1
y0=0.1
vx0=.1
vy0=.1
m=.1
t=0
dt=.01
x=x0
y=y0
vx=vx0
vy=vy0
X=[x]
Y=[y]
T=[t]

while t<=10:
    fx=-2*(y**2)*x*(1-x**2)*np.e**(-((x**2)+(y**2)))
    fy=-2*(x**2)*y*(1-y**2)*np.e**(-((x**2)+(y**2)))
    vx=vx+fx/m*dt
    vy=vy+fy/m*dt
    x=x+vx*dt
    y=y+vy*dt
    X.append(x)
    Y.append(y)
    T.append(t)
    t=t+dt
   
plt.plot(T,X)
plt.plot(T,Y)
plt.show()    