# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:57:45 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

x,y=[],[]
i=1
xlist = np.arange(0,10,.01)

while i<=1000:
    a=xlist[rand.randint(0,1000)]
    y.append(a**2)
    x.append(a)
    i=i+1

Mean=np.sum(y)/1000

MVT=10*Mean

plt.plot(x,y,'.')
plt.title("One random sample of Y values")
plt.xlabel("X")
plt.ylabel("X^2")
plt.show()
print("The mean of the function is: ",Mean)

print("The value of the integral, according to MVT is: ", MVT)

j=1
Means=[]
while j<=100:
    i = 1
    x,y=[],[]
    while i<=1000:
        a=xlist[rand.randint(0,1000)]
        y.append(a**2)
        x.append(a)
        i=i+1
    Means.append(np.sum(y)/100)
    j=j+1

plt.hist(Means)
plt.xlabel("Mean Values of Integral")
plt.show()
Meanofmeans=np.mean(Means)
MedianofMeans=np.median(Means)

print("The mean of the means of the intgral is: ",Meanofmeans)
print("The median of the means of the integral is: ",MedianofMeans) 
   
    
    