# -*- coding: utf-8 -*-

# bloc execute 101 fois
i = 0
while i < 100:
    if i % 2 == 1:
        print(i)
    i += 1
    
#bloc execute 49 fois
i = 1
while i < 100:
    print(i)
    i += 2

# bloc execute 101 fois
i = 100
while i >= 0:
    if i % 2 == 0:
        print(i)
    i -= 1
    
#bloc execute 50 fois
i = 100
while i >= 0:
    print(i)
    i -= 2

# suite de Fibonacci avec assignation double
f = 1
ff = 1
i = 1
print(f)
print(ff)
# i designe l'indice de ff
while i < 20:
    i += 1
    f, ff = ff, f + ff
    print(ff)

# suite de Fibonacci sans assignation double
f = 1
ff = 1
i = 1
print(f)
print(ff)
# n designe l'indice de ff, fff sert a permuter
while n < 20:
    n += 1
    fff = f + ff
    f = ff
    ff = fff
    print(ff)

#suite recurrente
u = 3
i = 0
# i designe l'indice de u
print(i, u)
while i < 9:
    u = i + 2*u
    i += 1
    print(i,u)

#nombre de triplets
#cpt designe le compteur
cpt = 0
z = 10
while z > 2:
    y = z - 1
    while y > 1:
        x = y -1
        while x >0:
            cpt += 1
            print(cpt,[x,y,z])
            x -= 1
        y -= 1
    z -= 1
print(cpt)

# suite de Fibonacci avec assignation double
n = 0
f = 1
ff = 1
#la phrase est vraie

print(f)
print(ff)

while n < 18 :
    n += 1
    ff, f = f + ff, ff
    print(ff) 