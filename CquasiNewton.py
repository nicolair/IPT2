# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 07:29:33 2015

@author: remy
"""
"""
p = 10
a = 3.
u = 0.5
#initialisation 
n = 0
x = u
while n < p:
    x = x*(2.-a*x)
    n += 1
    print(n,x)
"""

A = matrix([[7.,1.,11.,10.],[2.,6.,5.,2.],[8.,11.,3.,8.],[6.,9.,3.,6.]])
A = matrix([[1.,2.,3.],[4.,5.,6.],[7.,8.,10.]])

I = eye(3) #matrice I_3
J = 2*I

alpha = 19.*25.
alpha = 1/alpha
U = A.T  #initialisation avec la matrice transposée
U = alpha*U #avec une certaine normalisation 

X = U
truc = X*A - I
test = trace(truc * truc.T)
conv=[test]

while test>10**(-10):
    X = X*(J - A*X)
    n += 1
    truc = X*A - I
    test = trace(truc * (truc.T))
    conv.append(test)

plot(conv)
    



