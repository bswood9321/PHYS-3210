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
print("---------------------------")
print("Function: x^2, from 0-10")
print("Limit integration: ",Summation)    
    
Trapzsum = np.trapz(x**2,dx=.01)

print("Trapz integration: ",Trapzsum)

import scipy.integrate as ig
f = lambda x: x**2
ig.quad(f,0,10)
print("SciPy Integrate (Quadratic): ",ig.quad(f,0,10))

Simps=ig.simps(x**2,x,.01)
print("SciPy Integrate (Simpsons Rule): ",Simps)

print("The reason our summation formula is not very precise is that it is creating boxes of height x that are then added together to find the value of the integral." )
print("This means the width of the box is a finite value, instead in infinitessimal, and may cross over the function, giving us a value that is not very precise.")
print("-------------------------------------")
print("Function sin(100x) from 0-2Pi")

x1=np.arange(0,2*np.pi,np.pi/500)
y1=[]
i1=0
h1=(np.pi/500)
while i1<=999:
    func1=np.sin(100*x1[i1])
    y1.append(func1)
    i1=i1+1

Sum1=h1*np.sum(y1)
print("Limit Integration: ",Sum1)
Trapzsum1= np.trapz(np.sin(100*x1),dx=(np.pi/500))
print("Trapz Integration: ",Trapzsum1)
f1 = lambda x1: np.sin(100*x1)
print("SciPy Integrate (Quadratic): ",ig.quad(f1,0,np.pi*2))
print("SciPy Integrate (Simpsons Rule): ",ig.simps(np.sin(100*x1),x,np.pi/500))
print("--------------------------------------")

x2=np.arange(0,2*np.pi,np.pi/500)
y2=[]
i2=0
h2=(np.pi/500)
while i2<=999:
    a=x2[i2]
    func2=(np.sin(100*a))**a
    y2.append(func2)
    
    i2=i2+1

Sum2=h2*np.sum(np.nan_to_num(y2))
print("sin^x(100x)")
print("Limit Integration: ",Sum2)
print("This is the only type of integration I have been able to do, as I keep getting NaN and double scalar errors")
print("-------------------------------")
