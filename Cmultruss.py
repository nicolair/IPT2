#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:17:38 2017

@author: remy
"""

def multruss(a,b):
    m = 0
    while b > 0:
        if b % 2 == 1:
            m += a
            b -= 1
        else:
            a *= 2
            b = b //2
    return m

print(multruss(6,7))