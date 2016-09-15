# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 20:54:33 2015

@author: remy
"""

def compte(A,m):
    C = [0]*(m+1)
    for v in A:
        C[v] += 1
    return C

def croissant(C,n):
    A = []
    v = 0
    while v < len(C):
        nbo = C[v]
        while nbo >0:
            A.append(v)
            nbo -= 1
        v += 1
    return A

def crible(n):
    cricri = [True] * (n+1)
    cricri[0] = cricri[1] = False
    p = 2
    while p * p <= n:
        if cricri[p]:
            k = p * p
            while k <= n:
                cricri[k] = False
                k += p
        p += 1
    return cricri


def prefactor(n):
    F = [0] * (n+1)
    p = 2
    while p * p <= n:
        if F[p] == 0:
            k = p * p
            while k <= n:
                if F[k] == 0:
                    F[k] = p
                k += p
        p += 1
    return F
    
n = 100
lili = crible(n)
i = 0
while i <= n:
    if lili[i] :
        print(i)
    i = i+1
"""    
n = 5000
F = prefactor(n)
x = 4893
facteursPrem = []
while F[x] > 0:
    facteursPrem.append(F[x])
    x //= F[x]
facteursPrem.append(x)

print(facteursPrem)
t = 1
for v in facteursPrem:
    t *= v
print(t)
"""  

