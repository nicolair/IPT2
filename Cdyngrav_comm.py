L = []
L[0]=1
print(L)

"""
def smul(coeff,lili):
    n = len(lili)
    return [coeff*lili[i] for i in range(n)]

def smul(coeff,lili):
    return [coeff*v for v in lili]
    
def smul(coeff,li):
        n=len(li)
        L=[]
        for i in li:
            L.append(i*coeff)
    return L
"""    
def smul(coeff,L):
    T = L
    l = len(T)
    for i in range(l):
        T[i] = coeff*T[i]
    return T
    
L = [1,2,3]
print(smul(3,L))
print(L)

for v in range(4):
    print(v)

for v in range(1,4):
    print(v)
    
a,b,c = [1,2,3]
print(a,b,c)

L = []
L[0] = 2