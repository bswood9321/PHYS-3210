# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt



N = int(input("Pick a number: "))

n, a, sum1, m, b, sum2 = 1, 0, 0, N, 0, 0


while (n<=N):
    a = 1/n
    sum1+=a
    n = n+1
    
while (m>=1):
    b = 1/m
    sum2+=b
    m = m-1
    
error = (sum1 - sum2)/(np.absolute(sum1)+np.absolute(sum2))
print("For N = :",N,", the error is: ",error)

N1=1
Ns=[]
Errors=[]

while N1<=N:

    n1, a1, sum11, m1, b1, sum21 = 1, 0, 0, N1, 0, 0


    while (n1<=N1):
        a1 = 1/n1
        sum11+=a1
        n1 = n1+1
    while (m1>=1):
        b1 = 1/m1
        sum21+=b1
        m1 = m1-1

    Ns.append(N1)
    error1 = (sum11 - sum21)/(np.absolute(sum11)+np.absolute(sum21))
    Errors.append(error1)
    N1=N1+1
    
plt.plot(Ns,Errors,'r-')
plt.xlabel("N")
plt.ylabel("Error(x10^-16)")
plt.title("N vs. Error")
plt.show()    
    
print("The down summation is more precise because the error of the number is proportional to the number you are summing, therefore as the number decreases, there is less error, versus starting with a small number, and adding more error for every summation.")
    