#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:53:13 2018

@author: remy
"""
L1 = [ 1,1,2,4,6]
L2 = [2,2,3,3,3,5,7,8]

l1 = len(L1)
l2 = len(L2)
i1 = 0
i2 = 0
L3 = []
while i1 < l1 and i2 < l2:
    if L1[i1] <= L2[i2]:
        L3.append(L1[i1])
        i1 += 1
    else:
        L3.append(L2[i2])
        i2 += 1

while i1 < l1:
    L3.append(L1[i1])
    i1 += 1

while i2 < l2:
    L3.append(L2[i2])
    i2 += 1

