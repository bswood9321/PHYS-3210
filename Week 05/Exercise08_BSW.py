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
fdiff = fdiff = ((np.sin(x+np.pi/100))-np.sin(x))/((x+np.pi/100)-x)
plt.plot(x,fdiff)
plt.plot(x,derivative)
plt.title("Forward Difference Equation vs. Cosine function")
plt.show()