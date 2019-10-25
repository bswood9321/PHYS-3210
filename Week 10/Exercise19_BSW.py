# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:01:29 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

k=int(input('Enter a spring constant: '))
m=int(input('Enter a mass: '))
dt=.01
t=0
x=int(input('Enter a starting position: '))
v=int(input('Enter a starting velocity: '))
p=int(input('Enter an EVEN p-value between 2-12: '))
T=[t]
X=[x]
V=[v]

while t<15:
    f=-k*x**(p-1)
    v=v+(f/m)*dt
    x=x+v*dt
    t=t+dt
    T.append(t)
    X.append(x)
    V.append(v)
    
plt.plot(T,X,label='position')
plt.plot(T,V,label='velo')
plt.grid()
plt.legend(loc=(1.04,0))
plt.xlabel('Time')

plt.show()    

## 1. Yes, I get the result that I expect, a sinusoidal pattern of the spring "bouncing" back and forth. 
## 2. Yes, no matter what p value we choose, the solution does remain periodic with a constant amplitude. Some of them look really cool.
## 3. The mass has its highest velocity as the spring crosses "zero" in either direction. This does make sense as before this point,
## the mass is still acceleration faster, and after this point, it is de-accelerating until it reaches its maximum x value.
## 4. Yes, oscillators with different amplitudes have different periods. We can probably "design" two different amplitudes with the same periods,
## but it would require different masses and/or spring constants. 

k1=3
m1=2
x1=0
v1=5
p1=2

while p1<=12:
    t1=0
    T1=[t1]
    X1=[x1]
    V1=[v1]
    while t1<15:
        f=-k1*x1**(p1-1)
        v1=v1+(f/m1)*dt
        x1=x1+v1*dt
        t1=t1+dt
        T1.append(t1)
        X1.append(x1)
        V1.append(v1)
    plt.plot(T1,X1,label='position')
    plt.plot(T1,V1,label='velo')
    plt.legend(loc=(1.04,0))
    plt.show()
    print('P=',p1,', k=3, m=2')
    p1=p1+2
 