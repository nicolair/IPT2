# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:29:53 2014

@author: remy
"""
n = 40
u = 11./2.
uu = 61./11.
print(u,uu)
for i in range(3,n):
    uuu = 111 - 1130/uu + 3000/(uu*u)
    u = uu
    uu = uuu
    print(uu)

"""
n = 40

import sympy
X = sympy.symbols('X')
P = (X-5)*(X-6)*(X-100)
P = sympy.expand(P)
print(P)

import sympy
u = sympy.Rational(11,2)
uu = sympy.Rational(61,11)
print(u,uu)
for i in range(3,n):
    uuu = 111 - 1130/uu + 3000/(uu*u)
    u = uu
    uu = uuu
    print(uu, uu.evalf())

def bonindice(u,uu):
  eps = 1.0E-5
  #print(eps)
  n = 40
  i = 0
  while  abs(uu-100) > eps and i < n:
    uuu = 111. - 1130./uu + 3000./(uu*u)
    u = uu
    uu = uuu
    i += 1
    #print(uu)
  return i
  
#print(bonindice(5.5,5.3))

#import numpy as np
import matplotlib.pyplot as plt
xmin = 0.1
xmax = 10.
ymin = 0.1
ymax = 10
nx = 2000
ny = 2000
pasx = (xmax-xmin)/nx
pasy = (ymax-ymin)/ny
Lx = [xmin + i*pasx for i in range(0,nx)]
Ly = [ymin + i*pasy for i in range(0,ny)]

for x in Lx:
    for y in Ly:
        if bonindice(x,y) > 11:
            print(x,y,bonindice(x,y))
            plt.plot([x],[y],'.r')

plt.show()
"""