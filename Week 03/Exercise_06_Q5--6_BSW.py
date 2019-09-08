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



M, N = 0, 1000 

Distance = list() 
Walker = list() 

while(M<=99): 
    walker1=walk(N) 
    Distance.append(np.sqrt((walker1[0][-1]**2)+(walker1[1][-1]**2))) 
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
# As we see here, There are is no real theme to how far the walker gets from the origin. 
# most will be kind of concentrated in an area between roughly 20 and 40 units.
# Also to note, I could not quite figure out how to get the histogram to not use int so
#it is counting everything to the nearest whole number.

# I think this is fairly in line iwth what I would expect. Over any N number of random steps,
# the walker is going to have a range where most of them will end up. As N increases, that increases,
# but there will always be some walkers on the extremes.




# Question 6: Before this class I had never really heard of random walkers, so I don't know
# what real world applications they hold. I imagine there could be several ways they can used in modeling
# things in climate, finance, etc. while limiting certain parameters. I am excited to do this though. It has been fun
# doing htis exercise.






