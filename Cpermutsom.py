# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 15:48:28 2014

@author: remy
"""
import math as m
"""
n = 507 # un entier >= 2
nini = 1.
pepe = 2.
S = 0
while nini<= n and pepe <= n:
    S += 1/nini -1/pepe 
    nini += 2
    pepe += 2
if nini < n:
    S += 1/nini
"""
"""    
n = 50000 # un entier >= 2
p = 2. ; i = 1.
nini = 1. ; pepe = 2. ; S = 0
cptE = 0
while cptE < n:
    cpt = 0
    while cpt < i:
      S += 1/nini 
      nini += 2
      cpt += 1
    cpt = 0
    while cpt < p:
      S += -1/pepe
      pepe += 2
      cpt += 1
    cptE += 1
print(S-m.log(1+i/p))
"""

x = 1.1
nini = 1; pepe = 2; S = 0. ; fifi = []
eps = 1E-3
while S <= x- eps or x < S:
    while S < x:
        fifi.append(nini)
        S += 1/float(nini)
        nini += 2
    while x < S :
        fifi.append(pepe)
        S += -1/float(pepe)
        pepe += 2
        

print(S); print(fifi)
