# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def resul_sup(S,Y):
    n = len(S)
    X = [ 0 for i in range(n)]
    i = n-1
    while i >= 0:
        X[i] = Y[i][0]
        j = n-1
        while j > i:
            X[i] -= S[i][j]*X[j]
            j -= 1
        X[i] = X[i]/S[i][i]
        i -= 1
    return [ [v] for v in X]

def resul_inf(S,Y):
    n = len(S)
    X = [ 0 for i in range(n)]
    i = 0
    while i < n:
        X[i] = Y[i][0]
        j = 0
        while j < i:
            X[i] -= S[i][j]*X[j]
            j += 1
        X[i] = X[i]/S[i][i]
        i += 1
    return [ [v] for v in X]
    
def transpose(M):
    n = len(M)
    T = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            T[i][j] = M[j][i]
    return T
    
S = [[2,2,3,4], [0,1,2,3],[0,0,1,2],[0,0,0,1]]
print(S, transpose(S))

I = [[2,0,0,0], [2,1,0,0],[1,2,3,0],[0,0,0,2]]
Y = [[1],[2],[3],[4]]
#X = resul_sup(S,Y)
X = resul_inf(I,Y)
X = np.array(X)
S = np.array(S)
I = np.array(I)
print(np.dot(I,X))

Z = [0, 3, 7, 13, 21, 30, 40, 53, 66, 82, 99, 117, 138, 159]
t = [ [1, 4*i , (4*i)**2] for i in range(14)]
V = np.array(t)
tV = np.transpose(V)
Y = np.dot(tV,Z)
A = np.dot(tV,V)
L = np.linalg.cholesky(A) #renvoie l
tL = np.transpose(L)
X1 = np.linalg.solve(L,Y)
X = np.linalg.solve(tL,X1)

def f(t):
    return X[0] + X[1]*t + X[2]*t**2

t = [4*i for i in range(14)]
plt.plot(t, Z, 'bo')
plt.plot(t, [f(4*i) for i in range(14)], 'r')

plt.show()
