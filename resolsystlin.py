# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 18:18:40 2014

@author: remy
"""

def chercherIndPiv(A,i):
    p = len(A) #taille de la matrice
    iP = i #indice prov. de plus gde valeur
    for k in range(i+1,p):
        if abs(A[k][i]) > abs(A[iP][i]):
            iP = k
    return iP
    
def permuter(A,i,j):
    p = len(A[0])
    for k in range(p):
        A[i][k] , A[j][k] = A[j][k] , A[i][k]
        
def ajouter(A,i,j,coeff):
    p = len(A)
    for k in range(p):
        A[i][k] +=  coeff*A[j][k]
        
def resol(A,Y):
  p = len(A)
  for i in range(p):
    iP = chercherIndPiv(A,i)
    if iP > i:
      permuter(A,i,iP)
      Y[i][0],Y[iP][0] = Y[iP][0],Y[i][0]
    for j in range(i+1,p):
      coeff = -A[j][i]/A[i][i]
      ajouter(A,j,i,coeff)
      Y[j][0] += coeff * Y[i][0]
  X = [0.]*p
  X[p-1] = Y[p-1][0]/A[p-1][p-1]
  i = p-2
  while i >= 0:
    X[i]=(Y[i][0]-\\
       sum(A[i][k]*X[k] \\
            for k in range(i+1,p)))/A[i][i]
    i -= 1
  return X
    
A =[[2., 2., -3.],[-2., -1., -3.],[6.,4.,4.]]
Y = [[2], [-5.], [16.]]
print(resol(A,Y))

#génération aléatoire de 5 points
import random as rdm
M =   [ (rdm.random()*10 , rdm.random()*10) for i in range(5) ]

# génération de la matrice du système
A = [0]*5
for i in range(5):
    x,y = M[i]
    A[i] = [x*x , y*y, x*y, x, y]
#print(A)
    
# second membre
Y = [[-1.],[-1.],[-1.],[-1.],[-1.]]
#print(Y)

E = resol(A,Y)
import numpy
EE = numpy.linalg.solve(A,Y)
print(E,EE)

def phi(E,P,t):
    a,b,c,d,e = E
    x,y = P
    num = 2.*a*x + c*y + d +(2.*b*y + c*x + e)*t
    den = a + (b*t + c)*t
    l = - num/den
    return x + l , y+t*l

def F(E,P):
    a,b,c,d,e = E
    x,y = P
    return a*x*x + b*y*y + c*x*y + d*x + e*y +1
    
#t = (M[1][1] - M[0][1])/(M[1][0] - M[0][0])
#print(M[1],phi(E,M[0],t))

import matplotlib.pyplot as plt
plt.clf()
for P in M:
    plt.plot(P[0],P[1],'bo')
    print(F(E,P))

t = [(M[i+1][1] - M[0][1])/(M[i+1][0] - M[0][0]) for i in range(4)]
tmin = min(t)
tmax = max(t)

#print(tmin, tmax)
n = 30
p = 5
pas = (tmax - tmin)/n
tt = tmin - p*pas
for i in range(n+2*p):
    P = phi(E,M[0],tt)
    plt.plot(P[0],P[1],'ro')
    tt += pas