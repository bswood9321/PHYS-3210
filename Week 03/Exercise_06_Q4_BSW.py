# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:50:39 2019

@author: Brandon
"""

import numpy as np 
import numpy.random as rand
import matplotlib.pyplot as plt

def walk(N): 
    
    rand.seed() 

    
    x = [0.0] 
    y = [0.0]

    
    for n in range(N): 
        x.append(x[-1] + (rand.random() - 0.5)*2.0) 
        y.append(y[-1] + (rand.random() - 0.5)*2.0) 
    
    return np.array(x), np.array(y) 



M, N = 0, 1000 #Setting variables for later

Distance = list() #Creating an empty list to hold the distances we will record
Walker = list() #Creating an empty list of the number of steps each walker takes

while(M<=99): 
    walker1=walk(N) #Our walkers
    Distance.append(np.sqrt((walker1[0][-1]**2)+(walker1[1][-1]**2))) #Appending the Distance list with the distances of each walker
    Walker.append(N) # Appending the Walker list with the number of steps the walker has taken
    M = M+1 #Increasing our M value to progress the while loop
    N = N+45 #Increasing our N value to change our walker's number of steps
    
plt.plot(Walker, Distance, 'r+')
plt.xlabel("Number of steps")
plt.ylabel("Distance from the origin")
plt.show()

# By looking at the plot we receive, we can fairly well determine that the distance
# from the origin is fairly random, and does not necessarily increase, decrease, or 
# stagnate as the N value of the walker changes.This is exactly as I imagined would happen. 
# there is no reason why the distance should stay around any particular number. In fact,
# I believe if we plotted the average dsitance for several iterations of this code, we would find
# a similar plot of seemingly random values.