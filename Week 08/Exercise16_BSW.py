# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:01:19 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import timeit
import time

m=np.arange(0,2,.01)
fa=np.tanh(m/0.5)-m
fb=np.tanh(m/0.75)-m
fc=np.tanh(m/1)-m
fd=np.tanh(m/1.5)-m
fe=np.tanh(m/2)-m


plt.plot(m,fa,label='t=0.5')
plt.plot(m,fb,label='t=0.75')
plt.plot(m,fc,label='t=1')
plt.plot(m,fd,label='t=1.5')
plt.plot(m,fe,label='t=2')
plt.legend()
plt.xlabel('m')
plt.ylabel('tanh(m/t)-m')
plt.grid()
plt.show()


fa1 = lambda m: np.tanh(m/0.5)-m


print('The zero point for t=0.5, using bisect= :',op.bisect(fa1,0.75,1,xtol=1e-16))
print('The zero point for t=0.5,using N-R= ',op.newton(fa1,0.9))
print('---------------')

fa2 = lambda m: np.tanh(m/0.75)-m

print('The zero point for t=0.75, using bisect= :',op.bisect(fa2,0.75,1,xtol=1e-16))
print('The zero point for t=0.75,using N-R= ',op.newton(fa2,0.75))
print('---------------')

fa3 = lambda m: np.tanh(m)-m

print('The zero point for t=1, using bisect= :',op.bisect(fa3,0,.5,xtol=1e-16))
print('The zero point for t=1,using N-R= ',op.newton(fa3,0))
print('---------------')
print('There are no solutons for t>=1 because the function never goes above zero, as t is realted to the Curie temperature.')
print('Above this temperature, magnetism begins to break down')
print('---------------')


start1=timeit.timeit()
op.bisect(fa1,0.75,1,xtol=1e-16)
end1=timeit.timeit()
print('the time to calculate the zero point for 0.5 using bisect was: ',end1-start1,'s')
print('---------------')
time.sleep(.001)
start2=timeit.timeit()
op.newton(fa1,0.9)
end2=timeit.timeit()
print('the time to calculate the zero point for 0.5 using N-R was: ',end2-start2,'s')

time.sleep(.001)
start3=timeit.timeit()
op.bisect(fa1,0,7,xtol=1e-16)
end3=timeit.timeit()
print('--------------')
print('The time to calculate the zero point for 0.5, with a wider range fo values was: ',end3-start3,'s')