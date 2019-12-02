# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:26:02 2019

@author: BSWOOD9321
"""
import numpy as np
import matplotlib.pyplot as plt
e0=8.8541878128e-12
echarge=1.60217662e-19
hbar=1.0545718e-34
me=9.10938356e-31
a0=5.29177210903e-11
c=299792458
h=6.6260693e-34
def r(n):
    rn=(4*np.pi*e0*(hbar**2)*n**2)/(me*(echarge**2))
    return rn/a0

def E(n):
    En=-((me*(echarge**4))/(32*(np.pi**2)*(e0**2)*(hbar**2)))*(1/(n**2))
    En=En*6.242e18
    return En
def v(n):
    vn=hbar/(me*a0*n)
    return vn

def p(n):
    pn=hbar/(a0*n)
    return pn/1e-24

def Ze(z,n):
    Zn=-((me*(z**2)*(echarge**4))/(32*(np.pi**2)*(e0**2)*(hbar**2)))*(1/(n**2))
    Zn=Zn*6.242e18
    return Zn

def delE(m,n):
    delE=np.absolute(E(m)-E(n))
    return delE

def photonwavel(delE):
    l=h*c/(delE*1.60218e-19)
    return l

def photonfreq(l):
    f=c/l
    return f


n=1
Es=[]
radii=[]
Vs=[]
Ps=[]
while n<=10:
    e=E(n)
    rs=r(n)
    vs=v(n)
    ps=p(n)
    radii.append([rs,rs])
    Es.append([e,e])
    Vs.append([vs,vs])
    Ps.append([ps,ps])
    n=n+1



x=[1,2]
plt.figure(figsize=(1.5,6))
plt.plot(x,Es[0],'w')
plt.plot(x,Es[1],'w')
plt.plot(x,Es[2],'w')
plt.plot(x,Es[3],'w')
plt.plot(x,Es[4],'w')
plt.plot(x,Es[5],'w')
plt.plot(x,Es[6],'w')
plt.plot(x,Es[7],'w')
plt.plot(x,Es[8],'w')
plt.plot(x,Es[9],'w')
plt.xlim(1.1,1.9)
plt.yticks([-13.6, -3.4, -1.5, -.85, -.2],('n=1, -13.6eV','n=2, -3.4eV','n=3, -1.5eV','n=4,0.85eV','n=5+'))
plt.xticks([])
plt.title('Energy Levels of a Hydrogen Atom electron')
plt.show()


plt.figure(figsize=(1.5,6))
plt.plot(x,radii[0],'w')
plt.plot(x,radii[1],'w')
plt.plot(x,radii[2],'w')
plt.plot(x,radii[3],'w')
plt.plot(x,radii[4],'w')
plt.plot(x,radii[5],'w')
plt.plot(x,radii[6],'w')
plt.plot(x,radii[7],'w')
plt.plot(x,radii[8],'w')
plt.plot(x,radii[9],'w')
plt.xlim(1.1,1.9)
plt.yticks([1,4,8,16,25,36,49,64,81,100])
plt.xticks([])
plt.title('Quantized Radii of electron [Bohr radii]')
plt.show()

plt.figure(figsize=(1.5,6))
plt.plot(x,Vs[0],'w')
plt.plot(x,Vs[1],'w')
plt.plot(x,Vs[2],'w')
plt.plot(x,Vs[3],'w')
plt.plot(x,Vs[4],'w')
plt.plot(x,Vs[5],'w')
plt.plot(x,Vs[6],'w')
plt.plot(x,Vs[7],'w')
plt.plot(x,Vs[8],'w')
plt.plot(x,Vs[9],'w')
plt.xlim(1.1,1.9)
plt.yticks([2.2e6,1.1e6,7.3e5,5.5e5,4.4e5,3.6e5],('2.2e6','1.1e6','7.3e5','5.5e5','4.4e5','n=6+'))
plt.xticks([])
plt.title('Quantized Velocity of electron [m/s]')
plt.show()

plt.figure(figsize=(1.5,6))
plt.plot(x,Ps[0],'w')
plt.plot(x,Ps[1],'w')
plt.plot(x,Ps[2],'w')
plt.plot(x,Ps[3],'w')
plt.plot(x,Ps[4],'w')
plt.plot(x,Ps[5],'w')
plt.plot(x,Ps[6],'w')
plt.plot(x,Ps[7],'w')
plt.plot(x,Ps[8],'w')
plt.plot(x,Ps[9],'w')
plt.xlim(1.1,1.9)
plt.yticks([2,1,.66,.5,.4,.33],('2','1','.66','.5','.4','n=6+'))
plt.xticks([])
plt.title('Quantized momenta of electron [e-24 kg.m/s]')
plt.show()

zs=2

ZEs=[]
while zs<=5:
    zes=Ze(zs,1)
    ZEs.append([zes,zes])
    zs=zs+1
    
plt.figure(figsize=(1.5,6))
plt.plot(x,ZEs[0])
plt.plot(x,ZEs[1])
plt.plot(x,ZEs[2])
plt.plot(x,ZEs[3])
plt.xlim(1.1,1.9)
plt.yticks([-54.43,-122.46,-217.71,-340.17],('He(-54.43Ev)','Li(-122.46eV)','Be(-217.71eV)','B(-340.17eV)'))
plt.xticks([])
plt.title('n=1 Energy level for Z=2-5')
plt.show() 


m,n=10,2

BalmerphotonE=[]
Balmerphotonwavelength=[]
Balmerphotonfreq=[]
while m>n:
    BPE=delE(m,n)
    BPW=photonwavel(BPE)
    BPF=photonfreq(BPW)
    BPWref=BPW/1e-9
    BalmerphotonE.append(BPE)
    Balmerphotonwavelength.append([BPWref,BPWref])
    Balmerphotonfreq.append(BPF)
    m=m-1
    
plt.figure(figsize=(15,1.5))
ax=plt.axes()
ax.set_facecolor('black')
plt.plot(Balmerphotonwavelength[0],x, color='indigo')
plt.plot(Balmerphotonwavelength[1],x, color='indigo')
plt.plot(Balmerphotonwavelength[2],x, color='indigo')
plt.plot(Balmerphotonwavelength[3],x, color='indigo')
plt.plot(Balmerphotonwavelength[4],x, color='purple')
plt.plot(Balmerphotonwavelength[5],x, color='blue')
plt.plot(Balmerphotonwavelength[6],x, color='green')
plt.plot(Balmerphotonwavelength[7],x, color='red')
plt.ylim(1.1,1.9)
plt.xticks([396,410,434,485,656],('<---UV','410nm','434nm','486nm','656nm'))
plt.title('Balmer series Hydrogen Emission Spectrum')
plt.yticks([])
plt.show()




import numpy.linalg as la

min1=0.
max1=200.
u=0.5
b=10

def guass(npts,a,b,x,w):
    pp=0
    m=(npts+1)//2
    eps=3e-10
    for i in range(1,m+1):
        t=np.cos(np.pi*(float(i)-0.25)/(float(npts)+0.5))
        t1=1
        while ((np.absolute(t-t1))>=eps):
            p1,p2=1,0
            for j in range(1,npts+1):
                p3=p2
                p2=p1
                p1=((2*j-1)*t*p2-(j-1)*p3)/j
            pp=npts*(t*p1-p2)/(t*t-1)
            t1=t;t=t1-p1/pp
        x[i-1]=-t
        x[npts-i]=t
        w[i-1]=2/((1-t*t)*pp*pp)
        w[npts-i]=w[i-1]
    for i in range(0,npts):
        x[i]=x[i]*(b-a)/2 + (b+a)/2
        w[i]=w[i]*(b-a)/2

for M in range(16,32,8):
    z=[-1024, -512, -256, -128, -64,-32,-16,-8,-4,-2]
    for lmbda in z:
          A=np.zeros((M,M),float)
          WR=np.zeros((M),float)
          k=np.zeros((M),float)
          w=np.zeros((M),float)
          guass(M,min1,max1,k,w)
          for i in range(0,M):
              for j in range(0,M):
                  VR=lmbda/2/u*np.sin(k[i]*b)/k[i]*np.sin(k[j]*b)*k[j]
                  A[i,j]=2/np.pi*VR*k[j]*k[j]*w[j]
                  if (i==j):
                      A[i,j]+=k[i]*k[i]/2/u
          Es,evectors=la.eig(A)
          realev=Es.real
          for j in range(0,M):
              if (realev[j]<0):
                  print("M(size),lmbda,ReE=",M," ",lmbda, " ",realev[j])
                  break
              
                
