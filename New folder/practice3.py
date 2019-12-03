# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:17:53 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

G=6.67408e-11
MSun=1.989e30
MMe=3.285e23
MV=4.867e24
ME=6.046e24
MMa=6.417e23
MJ=1.899e27
MS=5.685e26
MU=8.682e25
MN=1.024e26


xsuninit=0
ysuninit=0
xearthinit=152.10e9
yearthinit=0
vxsuninit=0
vysuninit=0
vxearthinit=0
vyearthinit=29.29e3
vxsun=vxsuninit
vysun=vysuninit
vxearth=vxearthinit
vyearth=vyearthinit
xearth=xearthinit
yearth=yearthinit
xsun=xsuninit
ysun=ysuninit

XS=[xsun]
YS=[ysun]
XE=[xearth]
YE=[yearth]
VXS=[vxsun]
VYS=[vysun]
VXE=[vxearth]
VYE=[vyearth]

dt=1
t=0
T=[t]
while t<= (60*60*24*365):
    rs=np.sqrt(XS[-1]**2+YS[-1]**2)
    re=np.sqrt(XE[-1]**2+YE[-1]**2)
    theta=np.arctan(YE[-1]/XE[-1])
    F=((G*MSun*ME*(rs-re)/(np.absolute(rs-re))**3))
    Fx=F*np.cos(theta)
    Fy=F*np.sin(theta)
    vxearth=vxearth+Fx/ME*dt
    vyearth=vyearth+Fy/ME*dt
    xearth=xearth+vxearth*dt
    yearth=yearth+vyearth*dt
    XE.append(xearth)
    YE.append(yearth)
    VXE.append(vxearth)
    VYE.append(vyearth)
    T.append(t)
    t=t+dt
    
plt.plot(XE,YE)
plt.show()    