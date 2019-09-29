# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:04:25 2019

@author: BSWOOD9321
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

N_Ponds=[]
N=1000
M=1000
ValueofPi=[]
N_pond=0
i=0
j=1

while j<=1000:
    x=2*rand.random(1000)
    y=2*rand.random(1000)
    while i<=999:
        if np.sqrt((x[i]-1)**2+(y[i]-1)**2) <=1:
            N_pond+=1
        i=i+1
    j=j+1
    i=0
    N_Ponds.append(N_pond)
    ValueofPi.append(4*(N_pond/1000))
    N_pond=0
    
plt.plot(ValueofPi,N_Ponds,'r-')
plt.xlabel("Value of Pi")
plt.show()