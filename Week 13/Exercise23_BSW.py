# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:33:28 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt


#repeating path values, x0=.9, y0=.9, vx0=.21593090800323675, vy0=-.1, dt=.01



x0=.9
y0=.9
vx0=.21593090800323675
vy0=-.1

m=.1
t=0
dt=.0001
x=x0
y=y0
vx=vx0
vy=vy0
X=[x]
Y=[y]
T=[t]
Vx=[vx]
Vy=[vy]




while t<=100:
    fx=2*(y**2)*x*(x**2-1)*np.e**(-((x**2)+(y**2)))
    fy=2*(x**2)*y*(y**2-1)*np.e**(-((x**2)+(y**2)))
    vx=vx+fx/m*dt
    vy=vy+fy/m*dt
    x=x+vx*dt
    if np.abs(x)>=3:
        vx=-vx
    y=y+vy*dt
    if np.abs(y)>=3:
        vy=-vy
    X.append(x)
    Y.append(y)
    T.append(t)
    Vx.append(vx)
    Vy.append(vy)
    t=t+dt
   
plt.plot(T,X)
plt.plot(T,Y)
plt.show()

plt.plot(X,Y)
plt.show()

plt.plot(X,Vx)
plt.plot(Y,Vy)
plt.show()

x_v = np.arange(-10.0, 10.01, 0.01)
y_v = np.arange(-10.0, 10.01, 0.01)
X_v, Y_v = np.meshgrid(x_v, y_v)
Z_v = X_v**2 * Y_v**2 * np.exp(-(X_v**2 + Y_v**2))

fig, ax = plt.subplots(1,1, figsize=(10,8))

cb = ax.contourf(X_v, Y_v, Z_v, 10, cmap="Oranges")

ax.plot(X,Y,lw=2)
ax.set_xlim(-3.0, 3.0)
ax.set_xlabel("X Position")
ax.set_ylim(-3.0, 3.0)
ax.set_ylabel("Y Position")

cbar = fig.colorbar(cb)
cbar.ax.set_ylabel("Scattering Potential")

fig.tight_layout()
plt.show()