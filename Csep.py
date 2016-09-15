# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 16:55:16 2014

@author: remy
"""

def sep(L,v):
    l = len(L)
    g = 0
    d = l-1
    while g <= d:
        while g <= d and L[g] <= v:
            g += 1
        while g <= d and L[d] > v:
            d -= 1
        if g <= d:
            L[g],L[d] = L[d],L[g]
            g += 1
            d -= 1
    print(g)
        
L = [0,1,2,4,2,8,7,5,2,2,1,9]
print(L)
sep(L,4)
print(L)