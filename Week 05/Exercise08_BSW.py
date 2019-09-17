# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:03:34 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi,2*np.pi,np.pi/100)
sin = np.sin(x)
derivative = np.cos(x)
fdiff = ((np.sin(x+np.pi/100))-np.sin(x))/((x+np.pi/100)-x)
plt.plot(x,fdiff,label='Forward Difference Function')
plt.plot(x,derivative,'r--',label='Derivative[Cos(x)]')
plt.title("Forward Difference Equation and Cosine function")
plt.xlabel("x")
plt.legend(loc=(1.04,0))
plt.show()

grad = np.gradient(sin)
plt.plot(x,grad,label='Gradient command')
plt.plot(x,fdiff,'r--',label='Forward Difference Function')
plt.plot(x,derivative,'b-',label='Derivative[Cos(x)]')
plt.xlabel("x")
plt.title("ForDiff and Cos(x) and Gradient command")
plt.legend(loc=(1.04,0))
plt.show()