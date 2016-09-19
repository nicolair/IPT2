# -*- coding: utf-8 -*-

n = 1
f = 1
# la phrase est vraie

n = n + 1
f = n * f
# la phrase est encore vraie

while n <= 16 :
    n += 1
    f *= n
    # la phrase est encore vraie
    
print(n,f)