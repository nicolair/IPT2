#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:58:51 2018

@author: remy
"""

# Numération par les quotients.
b = 10
x = 200
#p puissance de b
#recherche du plus gd p <= x
p = 1
q = p * b
while q <= x:
    p = q
    q = p * b
#formation du dvloppement
resultat = ''
while p >= 1:
    resultat = resultat + str(x // p)
    x = x % p
    p = p // b
print(resultat) 

#tester en octal avec la fonction oct()

# Numération par les restes
b = 8
x = 5**123
print(oct(x))
resultat = ''
while x > 0 :
    resultat = str(x % b) + resultat
    x = x // b
print(resultat)  

