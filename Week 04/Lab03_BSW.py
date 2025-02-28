# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:50:39 2019

@author: Brandon
"""

import numpy as np 
import numpy.random as rand
import matplotlib.pyplot as plt

Polarity,Coordinates, X, Y, xtoss, ytoss, x, y = [],[],[],[],[],[],0,0

while not [x, y] in Coordinates:
   Coordinates.append([x,y])
   X.append(x)
   Y.append(y)
   xtoss.append(x)
   ytoss.append(y)
   P=rand.randint(-1,2)
   if P == -1:
       Polarity.append(1)
   else: 
       Polarity.append(0)
   R=rand.randint(0,1)
   if R==1:
       x = x+(rand.randint(-1,2))
       if x ==X[-1]:
           y = y+(rand.randint(-1,2))
           while y==Y[-1]:
               y=y+(rand.randint(-1,2))
   else:            
       y=y+(rand.randint(-1,2))
       if y==Y[-1]:
           x=x+(rand.randint(-1,2))
           while x==X[-1]:
               x=x+(rand.randint(-1,2))
   while [x,y] in Coordinates:
       if ([X[-1]+1,Y[-1]] in Coordinates) \
        and ([X[-1]-1,Y[-1]] in Coordinates) \
        and ([X[-1],Y[-1]+1] in Coordinates) \
        and ([X[-1],Y[-1]-1] in Coordinates):
           break
           
       else:
                 
           x=xtoss[-1]
           y=ytoss[-1]
           S=rand.randint(0,1)
           if S==1:
               x=x+(rand.randint(-1,2))
               if x==xtoss[-1]:
                   y=y+(rand.randint(-1,2))
                   while y==ytoss[-1]:
                       y=y+(rand.randint(-1,2))
           else:            
               y=y+(rand.randint(-1,2))
               if y==ytoss[-1]:
                   x=x+(rand.randint(-1,2))
                   while x==xtoss[-1]:
                       x=x+(rand.randint(-1,2))
                 
L=str(len(Coordinates)-1)
plt.plot(X,Y)
plt.title("Self-Avoiding Random Walker")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
print("The length of this protein chain is: ",L)                       
print(Polarity)
