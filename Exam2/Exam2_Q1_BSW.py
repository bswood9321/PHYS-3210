# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:54:26 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10,10,100)
y = (5/4)*x -2

plt.plot(x,y)
plt.grid()
plt.title("A linear equation; Y=5/4X-2")
plt.show()

y1=x**3-4

plt.plot(x,y1)
plt.grid()
plt.title("A nonlinear equation; y=X^3-4")
plt.show()

