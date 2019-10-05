# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import time

def powerResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    import datetime
    if seed == None:
        print("Seed value set to NONE, defaulting to system time.")
        seed=int(datetime.datetime.now().strftime("%H%M%S%f"))
        print(datetime.datetime.now().strftime("%H%M%S%f"))
    else:
        pass

    r = seed
    rando = []
    for i in range(N):
        rando.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    return rando[0:N]


Random1 = powerResidue(100)
plt.plot(Random1,'r')
plt.xlabel("N")
plt.ylabel("Value")
plt.title("First Random Sequence: N = 100; System Time Seed")
plt.show()

Random2 = powerResidue(100, 100, 25, 75, 50)
plt.plot(Random2,'r')
plt.xlabel("N")
plt.ylabel("Value")
plt.title("N=100, seed:100, a:25, c:75, M:50")
plt.show()

Random3 = powerResidue(100)
time.sleep(.001)
Random4 = powerResidue(100)
time.sleep(.001)
Random5 = powerResidue(100)

plt.plot(Random3)
plt.plot(Random4)
plt.plot(Random5)
plt.title("Three random sequences using Power Residue function")
plt.show()

XPR= powerResidue(100)
time.sleep(.003) # I had to add a pause because I kept getting a straight line
YPR= powerResidue(100)
XR=[]
YR=[]
i=1
while i<=100:
    XR.append(rand.random())
    YR.append(rand.random())
    i=i+1

plt.plot(XPR,YPR,'r.')
plt.title("Random scatter plot using powerResidue functions")
plt.show()

plt.plot(XR,YR,'k.')
plt.title("Random scatter plot using Numpy's random function")
plt.show()


plt.plot(XPR,YPR,'r.')
plt.title("The random scatter plots over each other")
plt.plot(XR,YR,'k.')
plt.show()






    