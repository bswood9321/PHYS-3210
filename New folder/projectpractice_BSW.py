# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:26:02 2019

@author: BSWOOD9321
"""
import numpy as np
import matplotlib.pyplot as plt

def E(n):
    En=-((me*(echarge**4))/(32*(np.pi**2)*(e0**2)*(hbar**2)))*(1/(n**2))
    En=En*6.242e18
    return En

n=1
Es=[]
while n<=10:
    e=E(n)
    Es.append([e,e])
    n=n+1



x=[1,2]
plt.figure(figsize=(1.5,6))
plt.plot(x,Es[0],'k')
plt.plot(x,Es[1],'k')
plt.plot(x,Es[2],'k')
plt.plot(x,Es[3],'k')
plt.plot(x,Es[4],'k')
plt.plot(x,Es[5],'k')
plt.plot(x,Es[6],'k')
plt.plot(x,Es[7],'k')
plt.plot(x,Es[8],'k')
plt.plot(x,Es[9],'k')
plt.xlim(1.1,1.9)
plt.yticks([-13.6, -3.4, -1.5, -.85, -.2],('n=1, -13.6eV','n=2, -3.4eV','n=3, -1.5eV','n=4,0.85eV','n=5+'))
plt.xticks([])
plt.title('Energy Levels of a Hydrogen Atom electron')
plt.show()

