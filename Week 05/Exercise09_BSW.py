# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:59:36 2019

@author: BSWOOD9321
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
print("Limit integration: ",Summation)    
    
Trapzsum = np.trapz(x**2,dx=.01)

print("Trapz integration: ",Trapzsum)
    