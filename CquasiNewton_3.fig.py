# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 07:29:33 2015

@author: remy

p = 10
a = 3.
u = 1
#initialisation 
n = 0
x = u
while n < p:
    x = x*(2.-a*x)
    n += 1
    print(n,x)
"""
L = [[7.,1.,11.,10.],[2.,6.,5.,2.],[8.,11.,3.,8.],[6.,9.,3.,6.]]
print(L)

A = matrix([[7.,1.,11.,10.],[2.,6.,5.,2.],[8.,11.,3.,8.],[6.,9.,3.,6.]])
A = matrix([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])

I = eye(3) #matrice I_3
J = 2*I
#print(A)
#print(A.T)
#print(A*B)

alpha = 19.*25.
alpha = 1/alpha
U = A.T  #initialisation avec la matrice transposée
U = alpha*U #avec une certaine normalisation 

X = U
truc = X*A - I
test = trace(truc * truc.T)
conv=[test]
n = 0
while test>10**(-10) and n < 30 :
    X = X*(J - A*X)
    n += 1
    truc = X*A - I
    test = trace(truc * (truc.T))
    conv.append(test)

plot(conv)




