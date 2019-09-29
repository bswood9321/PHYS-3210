# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:11:59 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand


y = []

i=1
while i<=1000000:
    a=rand.random(10)
    y.append((np.sum(a)**2))
    i=i+1
Mean=np.sum(y)/1000000

print("For a 10 dimensional integral from 0-1 for the function (x1+x2+x3...+x10)^2: ")
print("The mean value is: ",Mean)
    


y1=[]
M=[] 
N=2
error=[]
while N<=100:
    i=1
    while i<=N:
        a=rand.random(10)
        b=np.sum(a)**2
        y1.append(b)
        i=i+1
    MeanN=np.sum(y1)/N
    error.append(np.absolute(((155/6)-b)/(155/6)))
    M.append(1/np.sqrt(N))
    N=N+1
    
plt.plot(M,error,'+')
plt.xlabel("1/sqrt(N), [N from 1-100]")
plt.ylabel("Error")
plt.title("Error plot")
plt.show()

#Limit integration should only be reasonable up to where the number of calculations would be on the order of 10^6 or 10^7.
# For an N of 100, this would be around 3 dimensions, but to go to N of 10^5 or 10^6, then only one dimensional integrations 
# are really possible with limit integration.