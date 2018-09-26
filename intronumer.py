#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:58:51 2018

@author: remy
"""

#Numération par les quotients.
b = 8
x = 259
p = 1
#recherche du plus petit n tel que x<b^n
while p <= x:
    p *= b
#formation du développement
resultat = ''
p = p//b
while x>0:
    resultat = resultat + str(x // p)
    x = x % p
    p = p // b
print(resultat) 


#numération par les restes
b = 8
x = 5**123
print(oct(x))
resultat = ''
while x > 0 :
    resultat = str(x % b) + resultat
    x = x // b
print(resultat)  

