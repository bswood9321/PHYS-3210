# -*- coding: utf-8 -*-
"""
Exercise 03: Chapter 03, Kinder & Nelson

A common way to determine the value of a function is to sum over a series. 
For example, the Maclaurin series for sin(x) is

    sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...

Perform a series expansion to derive the equation above. Next, write down 
a general expression for the sum of the series that is valid between n = 0 
and n = N, where N ≥ 0. This will serve as your algorithm for summing 
the series.

One problem with the algorithm is that we do not know which value 
of N is suitable when calcualting the series. Instead of guessing, have 
your code proceed with the summation until the Nth term contributes a 
negligible amount to the final summation, say 1 part in 10**8.

Before writing any lines of code, discuss an approach with your neighbor 
and write out on paper how your code should proceed. Code up your approach 
in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(x) to 
      derive the equation in the README. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of x, the series converges.
   6. Which value for N was required to reach the desired precision and
      obtain convergence?
   7. Compare your results to the value determined using NumPy's sine 
      function.
   8. Steadily increase x and write down the relative error between your
      calculated value for sin(x) and the NumPy function's value. 
   9. What do you notice about the relative error?
  10. Will there be a time when the series does not converge? Make a plot
      of the relative error vs x to support your answer.

Created on Tue Aug 20 11:02:00 2019

@author: gafeiden
"""
import numpy as np
import matplotlib.pyplot as plt

# below is my basic approach for finding sin (x)

# first, we need to set our x at what we are trying to solve. Here, I have set x 
# equal to 200. A randomly chosen, yet large, number. 
# At the same time, we must make sure that n is set to zero, so the MacLaurin series 
# can properly sum from the 0th term.



x, n = 200, 0
sum = 0

# As I will show afterwards, large values of x will blow up and be impossible for
#a computer to calculate. However, as sin bounces between -1 and 1 around the unit circle,
# we can simply subtract 2pi a number of times, until x is sufficiently small, and we 
# will get the same result.


while (x>2*np.pi):
    x = x-(2*np.pi)

# Here is our MacLaurin series. I have set it up, as instructed, to only calculate until the
# term is sufficiently small. We have also created a variable, "sum", that will add up the terms
# this variable will be the result for the value of sin (x) we are calculating.

while (np.absolute((((-1)**n/(np.math.factorial(2*n+1))) * x**(2*n+1)))>(1/10**8)):

    a = (((-1)**n/(np.math.factorial(2*n+1))) * x**(2*n+1))
    sum+=a
    n = n+1
    
print(sum)    
# As stated previously, this will not work for large values of x.

#If we just run    
 
x, n, sum, = 50, 0, 0

while (np.absolute((((-1)**n/(np.math.factorial(2*n+1))) * x**(2*n+1)))>(1/10**8)):

    a = (((-1)**n/(np.math.factorial(2*n+1))) * x**(2*n+1))
    sum+=a
    n = n+1
    
    
# we will wither get a result that falls outside of the bounds of sin, or receive an error 
#because the computer cannot handle the calculation.
# This one happens to be calculable, but is well outside the bounds of sin.

print(sum)

#So, if we put our code to "shrink" x, back in:

while (x>2*np.pi):
    x = x-(2*np.pi)
    
#x becomes much smaller, and we are able to calculate it within the bounds of x.

# To know how accurate our MacLaurin series is, we can compare the result with the np.sin() function

sin = np.sin(x)

error = sum-sin
print (error)   

# By gradually increasing x, we find that around the x value of 35 is where the summation really 
# starts to separate itself from the actual sin() function. Prior to this point, the error was very,
# very small, on the order of 10^-9. Between 35 and 40, it has separated itself enough that the
#value we get using the MacLaurin series is outside of the bounds of the actual sin function.



























 

