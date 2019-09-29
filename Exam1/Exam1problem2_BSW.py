# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:07:01 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,.01)
y = [0]
i=1
h=.01
 
while i <=999:
    func = x[i]**2
    y.append(func)
    i=i+1
    
Summation = h*np.sum(y)
print("Function: x^2, from 0-10")
print("Limit integration from 0 to 10: ",Summation)    
    
x1 = np.arange(0,10,.01)
y1 = [0]
i1=999
h1=.01
j=0 
while i1 >=1:
    func1 = x1[j]**2
    y1.append(func1)
    i1=i1-1
    j=j+1
    
Summation1 = h1*np.sum(y1)
print("Function: x^2, from 0-10")
print("Limit integration from 10 to 0: ",Summation1)