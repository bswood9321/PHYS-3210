# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# HIV Prblem 5.1

import numpy as np, import matplotlib.plyplot as plt

# First we need to set up all of our arrays
# We will start with array "Time"

time = np.linspace(0,10,101)

#Now we will set up our Viral load array using the equation provided in the text book,
# along with the variables.

A, B, alpha, beta = 1, 0, 1, 1

viral_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)

#This creates an equal zied array as time with figures made from the equation. 
#the values for each variable are simply placeholders, except for B, which was given as zero

#Next we will pull the data given to us, and place it into two different arrays as we need

hiv_data = np.load("HIVseries.npz")

# As given, this data contains two different arrays, we will separate them now

time_in_days = hiv_data['time_in_days']
concentration = hiv_data['viral_load']

#Now we can plot these arrays as needed

#Through experimentation, I found that the best values for our variables are:

A, B, alpha, beta = 140000, 0, 0.42, 0

# As B is zerp, and the entire second part of the equation equals zero, it doesn't actually matter
# what the variable "beta" is set to. Here I set it to zero for ease.

#Now we can re-run our "viral_load" equation to repopulate the array with the updated values

viral_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)

# Now we can plot all of these arrays on a single plot to compare the values in the given data, vs. the 
# equation we have used/manipulated.

plt.plot(time_in_days, concentration,'r+'); 
plt.xlabel("Time[Days]"); plt.ylabel("Concentration"); 
plt.title("Viral load"); plt.plot(time, viral_load)

