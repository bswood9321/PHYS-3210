#
import numpy as np #importing different languages sets
import numpy.random as rand
import matplotlib.pyplot as plt

def walk(N): #defining our "walker".
    """ Function to compute an N-step random walk
    
        Input:
            N  ::  Total number of steps

        Output:
            x  ::  Array of all x positions
            y  ::  Array of all y positions

    """
    # seed random number generator
    rand.seed() #initializes random number generator, so everytime it runs it gives a new, but random, value

    # initialize x, y
    x = [0.0] 
    y = [0.0]

    # step in x-y space N times
    for n in range(N): 
        x.append(x[-1] + (rand.random() - 0.5)*2.0) # adds to the array, the last value in the array, + our formula for the next step
        y.append(y[-1] + (rand.random() - 0.5)*2.0) # same as x but for Y
    
    return np.array(x), np.array(y) #gives our values of x and y in an array


# Example simulation
walker_1 = walk(1000)   # compute path for 1000 steps

# Example plot of (x, y) pairs from example simulation 
plt.plot(walker_1[0], walker_1[1], '-') #plotting functions
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

