# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:54:26 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10,10,100)
y = (5/4)*x -2

plt.plot(x,y)
plt.grid()
plt.title("A linear equation; Y=5/4X-2")
plt.show()

y1=x**3-4

plt.plot(x,y1)
plt.grid()
plt.title("A nonlinear equation; y=X^3-4")
plt.show()
print('--------------------------------------------')
print('A first order DE is an equation with first derivative and the variables, '
      'for example, dy/dx +y=-x^2. These type of equations are fairly straight forward to solve, '
      'but can still be solved, in Python, using Eulers method, or an RK2 method')

t_i=0
x1=1
X=[x1]
T=[t_i]
dt=.01
t=t_i
while t<=(t_i+10):
    dxdt=4*np.sin(t)**2
    x1=x1+dxdt*dt
    t=t+dt
    X.append(x1)
    T.append(t)
    
plt.plot(T,X)
plt.grid()
plt.title("1st order DE")
plt.show()    
print('-------------------------------------------')
print('A fourth order DE is one that calculates a value based on the fourth derivative of a function ' 
      ' such as the Euler Bernoulli Beam Theory equation, E*I*d^4x/dw^4 = q(x)')

print('-------------------------------------------')
print('A coupled 1st ODE is one where you have multiple derivatives, such as '
      'dx/dt = q and dy/dt =p. We can use diffeq techniques to find x and y dependent upon t and solve similarly as any other.')

x2=1
y2=1
t_i1=0
X2=[x2]
Y2=[y2]
T2=[t_i1]
dt=.01
t2=t_i1
while t2<=(t_i1+10):
    dxdt=.25*x2*np.sin(t2)**4
    dydt=.25*y2*np.cos(t2)**4
    x2=x2+dxdt*dt
    y2=y2+dydt*dt
    X2.append(x2)
    Y2.append(y2)
    T2.append(t2)
    t2=t2+dt
plt.plot(T,X2)
plt.plot(T,Y2)
plt.show()
    
    
    
print('----------------------------------------')
print('Question 2: '
      'The difference between the Euler method and an RK2 method is that the Euler '
      'method uses a full step of dt to calculate the next value of x, where the RK2 '
      'method uses a half step value of the derivative to calculate the next value of x. '
      'In other words, the RK2 method is using the average value of the derivative between '
      'x and x+dx, rather than just the value of the derivative at x. This decreases the area '
      'of the "box" outside of the function that we would consider error when using the the value of the '
      'derivative at either x or x+dx. Again, in other words, the Euler method does not take into account the '
      'curvature of the function, where RK methods do. As we increase the value of the RK method, up to RK4 and beyond, '
      'the accuracy improves. An RK4 method would be perfectly accurate for any function of an order of 4 or less, for '
      'the same reason as above, it uses more steps inbetween evqaluating x values.')
