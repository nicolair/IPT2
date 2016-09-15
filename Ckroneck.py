# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 19:16:23 2014

@author: remy
"""

from sympy import polys
from sympy.abc import X
P = X**2+1
Q = X**3-1
T = (P*Q).expand()
#pour obtenir le reste d'une division entière
print 10 % 3
