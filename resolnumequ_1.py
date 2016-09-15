# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:32:01 2014

@author: remy
"""
import math
import matplotlib.pyplot as plt

def newt1(f,g,b,n):
    bb = b - f(b)/g(b)
    k = 0
    while k < n:
        b =bb
        bb = b - f(b)/g(b)
        k += 1
    return bb

def newt(f,g,b,eps):
    bb = b - f(b)/g(b)
    k = 0
    while abs(bb-b)> eps:
        b =bb
        bb = b - f(b)/g(b)
        k += 1
    return bb
eps = 0.0001
j = complex(math.cos(2*math.pi/3),math.sin(2*math.pi/3))
j2 = complex(math.cos(2*math.pi/3),-math.sin(2*math.pi/3))
    
def col(z):
    if(abs(z-1)<eps):
        return '.r'
    elif(abs(z-j)<eps):
        return '.b'
    elif(abs(z-j2)<eps):
        return '.g'
    else:
        return 0

def f(x): return x**3-1
def df(x): return 3*x**2

#z = newt(f,df, complex(1.,1.),eps)

#print(col(z))
xmin = 0.1
xmax = 10.
ymin = 0.1
ymax = 10
nx = 10
ny = 10
pasx = (xmax-xmin)/nx
pasy = (ymax-ymin)/ny
Lx = [xmin + i*pasx for i in range(0,nx)]
Ly = [ymin + i*pasy for i in range(0,ny)]

for x in Lx:
    for y in Ly:
        zi = complex(x,y)
        z = newt(f,df,zi,eps)
        if col(z) != 0:
            plt.plot([zi.real],[zi.imag],col(z))

#plt.show()

    
#def r(x): return x**2 -2.    
#def dr(x) : return 2*x

#r2 = math.sqrt(2)

#print(abs(newt(r,dr,2,4) - r2))
#courbe1 = [math.log(abs(newt(r,dr,2,2) - r2)) for i in range(1,5)]
#plot(courbe1)

