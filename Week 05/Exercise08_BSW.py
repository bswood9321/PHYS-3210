# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:03:34 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi,2*np.pi,np.pi/20)
sin = np.sin(x)
derivative = np.cos(x)
fdiff = ((np.sin(x+np.pi/20))-np.sin(x))/((x+np.pi/20)-x)
plt.plot(x,fdiff,label='Forward Difference Function')
plt.plot(x,derivative,'r--',label='Derivative[Cos(x)]')
plt.title("Forward Difference Equation and Cosine function")
plt.xlabel("x")
plt.legend(loc=(1.04,0))
plt.show()

grad = np.gradient(sin,np.pi/20)
plt.plot(x,grad,label='Gradient command')
plt.plot(x,fdiff,'r--',label='Forward Difference Function')
plt.plot(x,derivative,'b-',label='Derivative[Cos(x)]')
plt.xlabel("x")
plt.title("ForDiff and Cos(x) and Gradient command")
plt.legend(loc=(1.04,0))
plt.show()

Errorf = np.absolute(fdiff-derivative)/derivative

Errorg = np.absolute(grad-derivative)/derivative 

plt.plot(x,Errorf,label='Forward Differential Error')
plt.legend(loc=(1.04,0))
plt.show()
plt.plot(x,Errorg,label='Gradient Error')
plt.legend(loc=(1.04,0))
plt.show()

print("So there is a small difference between the two different ways to find the derivative.")
print("The errors of each, while at similar locations (it looks to be at the points where the derivative=0), have different values.")
print("This is probably due to how the functions calculate the values really close to zero.")

x1 = np.arange(-2*np.pi,2*np.pi,np.pi/20)
sin1 = np.sin(x1+.25)
derivative1 = np.cos(x1+.25)
fdiff1 = ((np.sin(x1+np.pi/20+.25))-np.sin(x1+.25))/((x1+np.pi/20)-x1)
plt.plot(x1,fdiff1,label='Forward Difference Function')
plt.plot(x1,derivative1,'r--',label='Derivative[Cos(x)]')
plt.title("Challenge Plot 1")
plt.xlabel("x")
plt.legend(loc=(1.04,0))
plt.show()

grad1 = np.gradient(sin1,np.pi/20)
plt.plot(x1,grad1,label='Gradient command')
plt.plot(x1,fdiff1,'r--',label='Forward Difference Function')
plt.plot(x1,derivative1,'b-',label='Derivative[Cos(x)]')
plt.xlabel("x")
plt.title("Challenge Plot 2")
plt.legend(loc=(1.04,0))
plt.show()

Errorf1 = np.absolute(fdiff1-derivative1)/derivative1

Errorg1 = np.absolute(grad1-derivative1)/derivative1 

plt.plot(x1,Errorf1,label='Forward Differential Error')
plt.legend(loc=(1.04,0))
plt.title("Challenge Error 1")
plt.show()
plt.plot(x1,Errorg1,label='Gradient Error')
plt.legend(loc=(1.04,0))
plt.title("Challenge Error 2")
plt.show()


x2 = np.arange(1,10,.20)
func = (x2**3)/3
derivative2 = x2**2
fdiff2 = (((x2+.20)**3)/3-((x2**3)/3)/.20)
plt.plot(x2,fdiff2,label='Forward Difference Function')
plt.plot(x2,derivative2,'r--',label='Derivative[x^2]')
plt.title("Bonus Plot 1")
plt.xlabel("x")
plt.legend(loc=(1.04,0))
plt.show()

grad2 = np.gradient(func,np.pi/20)
plt.plot(x2,grad2,label='Gradient command')
plt.plot(x2,fdiff2,'r--',label='Forward Difference Function')
plt.plot(x2,derivative2,'b-',label='Derivative[Cos(x)]')
plt.xlabel("x")
plt.title("Bonus Plot 2")
plt.legend(loc=(1.04,0))
plt.show()

Errorf2 = np.absolute(fdiff2-derivative2)/derivative2

Errorg2 = np.absolute(grad2-derivative2)/derivative2 

plt.plot(x2,Errorf2,label='Forward Differential Error')
plt.legend(loc=(1.04,0))
plt.title("Bonus Error 1")
plt.show()
plt.plot(x2,Errorg2,label='Gradient Error')
plt.legend(loc=(1.04,0))
plt.title("Bonus Error 2")
plt.show()
