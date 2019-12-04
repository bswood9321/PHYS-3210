# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:23:00 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

from mayavi import mlab



x1=np.linspace(1,10,10)
k=4
y1=k*x1**2
colors=[]
i=0
while i<=9:
    if y1[i]<100:
        colors.append("red")
    elif y1[i]<250:
        colors.append("orange")
    else:
        colors.append("blue")
    i=i+1

plt.plot(x1[0],y1[0],'+',color=colors[0])
plt.plot(x1[1],y1[1],'+',color=colors[1])
plt.plot(x1[2],y1[2],'+',color=colors[2])
plt.plot(x1[3],y1[3],'+',color=colors[3])
plt.plot(x1[4],y1[4],'+',color=colors[4])
plt.plot(x1[5],y1[5],'+',color=colors[5])
plt.plot(x1[6],y1[6],'+',color=colors[6])
plt.plot(x1[7],y1[7],'+',color=colors[7])
plt.plot(x1[8],y1[8],'+',color=colors[8])
plt.plot(x1[9],y1[9],'+',color=colors[9])
plt.yticks([y1[0],y1[5],y1[8]],(colors[0],colors[5],colors[8]))
plt.show()



x, y, z = np.ogrid[-25:25:200j, -25:25:200j, -25:25:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square(((r**2)/81)*(1/np.sqrt(6*np.pi))*(np.e**(-r/3))*((3*np.cos(theta)**2)-1))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("3d Hydrogen")
mlab.show()

x, y, z = np.ogrid[-25:25:200j, -25:25:200j, -25:25:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((np.sqrt(2)/81)*(1/(np.sqrt(np.pi)))*(np.e**(-r/3))*(6-r))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("3p Hydrogen")
mlab.show()

x, y, z = np.ogrid[-15:15:200j, -15:15:200j, -15:15:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((1/81)*(1/(np.sqrt(3*np.pi)))*(np.e**(-r/3))*(27-(18*r)+(2*r**2)))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("3s Hydrogen")
mlab.show()

x, y, z = np.ogrid[-10:10:200j, -10:10:200j, -10:10:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((1/4)*(1/np.sqrt(2*np.pi))*r*(np.e**(-r))*np.cos(theta))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("2p Hydrogen")
mlab.show()

x, y, z = np.ogrid[-10:10:200j, -10:10:200j, -10:10:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((1/(4*np.sqrt(2*np.pi))*(2-(r))*np.e**(-r/2)))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("2s Hydrogen")
mlab.show()

x, y, z = np.ogrid[-5:5:200j, -5:5:200j, -5:5:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((2/(np.sqrt(np.pi)))*np.e**(-r))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("1s Hydrogen")
mlab.show()
