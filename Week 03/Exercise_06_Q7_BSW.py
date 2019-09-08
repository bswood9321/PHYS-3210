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
    z = [0.0]
    
    for n in range(N): 
        x.append(x[-1] + (rand.random() - 0.5)*2.0) 
        y.append(y[-1] + (rand.random() - 0.5)*2.0) 
        z.append(z[-1] + (rand.random() - 0.5)*2.0)
    return np.array(x), np.array(y), np.array(z) 



M, N = 0, 1000 

Distance = list() 
Walker = list() 

while(M<=99): 
    walker1=walk(N) 
    Distance.append(np.sqrt((walker1[0][-1]**2)+(walker1[1][-1]**2)+(walker1[2][-1]))) 
    Walker.append(N) 
    M = M+1 
    N = N+45 
    
plt.plot(Walker, Distance, 'r+')
plt.xlabel("Number of steps")
plt.ylabel("Distance from the origin")
plt.show()



plt.hist(Distance, 100)
plt.xlabel("Distance")
plt.ylabel("Iterations (to nearest whole number)")
plt.title("Distance")
plt.show()


# I don't believe the results really changed at all for problem 5. If anything, I think it kind of 
# flattened the histogram somewhat. Less distances concentrated, and now spread out a little more.
# however, the min and max distances stayed pretty well the same.
