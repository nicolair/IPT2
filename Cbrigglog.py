# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 08:51:54 2014

@author: remy
"""
"""
str = "101010101010101010101010101"
l = len(str) -1
print(str,l)
x = int(str, base=2)
print(x*2**(-l))
print(4./3.)
"""

def add(A,B):
    l = len(A)
    S = [ 0 for i in range(l)]
    i = l-1
    ret = 0
    while i>=0:
        t = A[i] + B[i] + ret
        S[i] = t % 2
        ret = t // 2
        i -= 1
    return [ret,S]
    
def shift(A,k):
    l = len(A)
    i = l-1
    while i >= k:
        A[i] = A[i-k]
        i -= 1
    while i >= 0:
        A[i] = 0
        i -= 1
    
def carre(A):
    ret = 0
    C = [0 for a in A] 
    B = [a for a in A]
    d = 0
    for a in A:
        if a == 1:
            shift(B,d)
            truc = add(C,B)
            ret += truc[0]
            C = truc[1]
            d = 0
        d += 1
    return [ret,C]


A = [1,1,0,1,0]
print(A)
print(carre(A))
    