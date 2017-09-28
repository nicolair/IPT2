#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:37:06 2017

@author: remy
"""
n =2100

if n % 4 !=0:
    biss = False
elif n % 400 == 0 :
    biss = True
elif n % 100 == 0 :
    biss = False
else :
    biss = True
    
if biss:
    print(str(n) + ' est bissextile')
else:
    print(str(n) + " n'est pas bissextile")
    