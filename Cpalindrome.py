# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:58:44 2013

@author: remy
"""
def retournL(L):
    i = 0
    j = len(L) - 1
    while i < j:
        L[i] , L[j] = L[j] , L[i]
        i += 1
        j -= 1

#L = [1,2,3,4,5,6]
#print(L)
#retournL(L)
#print(L)

def decomp(n):
    p = 1
    while p <= n:
        p *= 10
    p = p // 10
    L = []
    while p >= 1:
        L.append( n // p)
        n = n % p
        p = p // 10
    return L

def comp(L):
    v = 0
    i = 0
    while i < len(L):
        v = 10*v + L[i]
        i += 1
    return v
    
#print(comp([1,2,3,4,5]))
def retournN(n):
    L = decomp(n)
    L.reverse()
    return comp(L)
    
def sym(n):
    return n + retournN(n)
    
def delta(n,p):
    i = 0
    s = retournN(n)
    while s != n and i <= p:
        n = n + s
        s = retournN(n)
        i += 1
    #print(n)
    return i
    
#print(delta(98,100))

p = 5000
n = 197
d = 0
nmax = 1
dmax = 0
while d <= p and n <= 300 :
    if d > dmax:
        dmax = d
        nmax = n
    n += 1
    d = delta(n,p)

print(n,nmax,dmax)
#print(sym(12345))
