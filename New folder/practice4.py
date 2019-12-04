# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:44:23 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

G=6.67408e-11
M1=4.8675e24
M2=5.9724e24
M3=2.5e30


x1=0
x2=0
x3=0
y1=32.1e5
y2=-28e5
y3=89e10
vx1=-34.78e3
vx2=29.29e3
vx3=-230
vy1=0
vy2=0
vy3=0
X1=[x1]
X2=[x2]
X3=[x3]
Y1=[y1]
Y2=[y2]
Y3=[y3]
dt=60
t=0
T=[t]
while t<=3000000:
    Fx1=G*M1*M2*X1[-1]/((X1[-1]**2+Y1[-1]**2)**1.5)
    Fy1=G*M1*M2*Y1[-1]/((X1[-1]**2+Y1[-1]**2)**1.5)
    Fx2=G*M1*M2*X2[-1]/((X2[-1]**2+Y2[-1]**2)**1.5)
    Fy2=G*M1*M2*Y2[-1]/((X2[-1]**2+Y2[-1]**2)**1.5)
    vx2=vx2+Fx2/M2*dt
    vy2=vy2+Fy2/M2*dt
    x2=x2+vx2*dt
    y2=y2+vy2*dt
    vx1=vx1+Fx1/M1*dt
    vy1=vy1+Fy1/M1*dt
    x1=x1+vx1*dt
    y1=y1+vy1*dt
    X1.append(x1)
    Y1.append(y1)
    X2.append(x2)
    Y2.append(y2)
    T.append(t)
    t=t+dt
    
plt.plot(X2,Y2)
plt.plot(X1,Y1)
plt.show()