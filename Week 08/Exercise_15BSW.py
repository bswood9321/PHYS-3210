# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:09:26 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt


Eb=np.arange(-10,100,.01)

f=np.sqrt(10-Eb)*np.tan((np.sqrt(10-Eb)))-np.sqrt(Eb)

plt.plot(Eb,f)
plt.xlabel("Energy of bound state")
plt.ylim(-10,10)
plt.xlim(-2,10)
plt.grid()
plt.show()

import scipy.optimize as op
f1 = lambda Eb: np.sqrt(10-Eb)*np.tan((np.sqrt(10-Eb)))-np.sqrt(Eb)


print("The zero points, using SciPy's bisect function is: ")
print(op.bisect(f1,8,9,xtol=1e-16))
print(op.bisect(f1,0,.01,xtol=1e-16))

print("The zero points, using SciPy's Newton function is: ")
print(op.newton(f1,7.6))
print(op.newton(f1,0))

print("Energy evaluated at zero points:")
print("8.592785275229836: ",f1(8.592785275229836))
print("0.0040192624533292335: ",f1(0.0040192624533292335))
print("8.59278527522984: ",f1(8.59278527522984))
print("0.004019262453329195: ",f1(0.004019262453329195))

f2 = np.sqrt(Eb)*(1/(np.tan(np.sqrt(10-Eb))))-(np.sqrt(10-Eb))

plt.plot(Eb,f2)
plt.ylim(-10,10)
plt.xlim(-1,10)
plt.grid()
plt.title("Secondary Equation")
plt.show()

f3 = np.sqrt(Eb)*(1/(np.tan(np.sqrt(20-Eb))))-(np.sqrt(20-Eb))

plt.plot(Eb,f3)
plt.ylim(-10,10)
plt.xlim(-10,20)
plt.grid()
plt.title("Secondary Equation-20")
plt.show()

f4 = np.sqrt(Eb)*(1/(np.tan(np.sqrt(30-Eb))))-(np.sqrt(30-Eb))

plt.plot(Eb,f4)
plt.ylim(-10,10)
plt.xlim(-10,20)
plt.grid()
plt.title("Secondary Equation-30")
plt.show()