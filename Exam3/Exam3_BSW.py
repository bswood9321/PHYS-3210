# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:54:43 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

h=1e-5
t=0
w0=0.4
T=1
g=2
gt=5
Einit=0.1
E_dtinit=0.1

Ts=[]
E=Einit
E_dt=E_dtinit
E_arr=[]
E_dt_arr=[]
E_dt2init=-w0**2*(E)-(1/T)*E_dt+(g-gt*(E)**2)*E_dt

while t<=30:
    E_dt2=-w0**2*(E)-(1/T)*E_dt+(g-gt*(E)**2)*E_dt
    E_dt=E_dt+E_dt2*h
    E=E+E_dt*h
    E_dt_arr.append(E_dt)
    E_arr.append(E)
    Ts.append(t)
    t=t+h
    
plt.plot(Ts,E_arr)
plt.show()
plt.plot(E_arr,E_dt_arr)
plt.show()