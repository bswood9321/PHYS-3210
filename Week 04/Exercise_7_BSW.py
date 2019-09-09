# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

def powerResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    import datetime
    if seed == None:
        print("Seed value set to NONE, defaulting to system time.")
        seed=int(datetime.datetime.now().strftime("%H%M%S%f"))
        print(datetime.datetime.now().strftime("%H%M%S%f"))
    else:
        pass

    r = seed
    rand = []
    for i in range(N):
        rand.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    return rand[0:N]


Random1 = powerResidue(100)
plt.plot(Random1,'r')
plt.xlabel("N")
plt.ylabel("Value")
plt.title("First Random Sequence: N = 100; System Time Seed")
plt.show()

Random2 = powerResidue(100, 100, 25, 75, 50)
plt.plot(Random2,'r')
plt.xlabel("N")
plt.ylabel("Value")
plt.title("N=100, seed:100, a:25, c:75, M:50")
plt.show()

Random3 = powerResidue(100)
time.sleep(.001)
Random4 = powerResidue(100)
time.sleep(.001)
Random5 = powerResidue(100)

plt.plot(Random3)
plt.plot(Random4)
plt.plot(Random5)
plt.show()
