# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:00:10 2019

@author: BSWOOD9321
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

xlist=[]
ylist=[]
count=[]
i = 1

while i <=10000:
    x=10*rand.random()
    y=100*rand.random()
    if y<=x**2:
        ylist.append(y)
        xlist.append(x)
        count.append(1)
    i=i+1

Int=np.sum(count)/(i/1000)

print("The value of the integral is: ",Int)

plt.plot(xlist,ylist,'r.')
plt.show()    


x2list=[]
y2list=[]
count2=[]
j=1
while j<=10000:
    x2=2*np.pi*rand.random()
    y2=rand.random()
    if y2<= np.absolute(np.sin(x2)):
        x2list.append(x2)
        if np.sin(x2)<0:
            y2list.append(-y2)
            count2.append(-1)
        else:
            y2list.append(y2)
            count2.append(1)
        
    j=j+1

Int2=np.sum(count2)/(j/10)

print("The value of the integral is: ", Int2)

plt.plot(x2list,y2list,'b.')
plt.show()    

x3list=[]
y3list=[]
count3=[]
k=1
while k<=10000:
    x3=10*np.pi*rand.random()
    y3=2*rand.random()
    if y3 <=np.absolute( (np.cos(x3))*np.sin(x3/2)*np.tan(x3/4)):
        x3list.append(x3)
        if (np.cos(x3))*np.sin(x3/2)*np.tan(x3/4)<0:
            y3list.append(-y3)
            count3.append(-1)
        else:
            y3list.append(y3)
            count3.append(1)
    k=k+1

Int3 = np.sum(count3)/(k/100)

print("The value of this integral is: ", Int3)

plt.plot(x3list,y3list,'g.')
plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    