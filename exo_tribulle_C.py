# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:44:07 2013

@author: remy
"""

def TriBulle(A):
    n = len(A)
    i = 0
    nbPerm = 0
    while i < n-1:
        if A[i]<A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]
            nbPerm += 1
            if i > 0:
                i -= 1
        else:
            i += 1
    return nbPerm

A = [1,2,4,5,1,47,52,35,14,41]
print(TriBulle(A))
print(A)