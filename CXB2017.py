#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:32:40 2017

@author: remy
"""

def membre(p,q):
    for pt in q:
        if p == pt:
            return True
    return False

q = [[1,1],[1,3],[2,4]]
print(membre([1,3],q))

def intersection(p,q):
    res = []
    for pt in p:
        if membre(pt,q):
            res.append(pt)
    return res

q1 = [[1,2],[1,3],[2,5],[1,1]]
print(intersection(q,q1))

def bits(x,k):
    bibin = bin(x)
    l = len(bibin)
    if k > l-3:
        return 0
    else :
        return int(bibin[-1-k])

print(bits(4,1))

def code(n,p):
    x = p[0]
    y = p[1]
    Lcode = []
    k = n - 1
    while k >= 0:
        c = 2*bits(x,k) + bits(y,k)
        Lcode.append(c)
        k -= 1
    return Lcode

print(code(3,[1,6]))

def compare_pcodes(n,c1,c2):
    k = 0
    while k < n and c1[k] == c2[k]:
        k += 1
    if k == n:
        return 0
    elif c1[k] < c2[k]:
        return 1
    else:
        return -1

print(compare_pcodes(3,[1,2,3],[1,3,3]))

def ksuffixe(n,k,q):
    q_res = list(q)
    i = n-1
    # k < n obligatoire
    while i > n-k-1 and q[i] == 4:
        i -= 1
    if i == n-k-1:
        q_res[i] = 4
    return q_res

print(ksuffixe(4,2,[0,1,4,4]))

def compacte(n, s):
    aql = s
    for k in range(n):
        aql_t = [] # pour stocker le k-eme compactage
        m = len(aql)
        i = 0
        while i < m - 3: 
            #pour 4 quadrants qui se suivent
            suff0 = ksuffixe(n, k, aql[i])
            suff3 = ksuffixe(n, k, aql[i + 3])
            
            if compare_pcodes(n, suff0, suff3) == 0:
                aql_t.append(suff0) 
                # 4 donnent 1 on compacte
                i += 4
            else : #pas de compactage
                aql_t.append(aql[i])
                i += 1
                
        for j in range(i,m): #on ajoute les derniers
            aql_t.append(aql[j])
        
        aql = aql_t
        
    return aql

def compare_ccodes(n,p,q):
    cpt = 0
    #on cpte les premiers elts egaux
    while cpt < n and p[cpt] == q[cpt]:
        cpt += 1
    if cpt == n: #P = Q
        return 0
    elif q[cpt] == 4: #P dans Q
        return 2
    elif p[cpt] == 4: #Q dans P
        return -2
    elif p[cpt] < q[cpt] :# disjoints et P < Q
        return 1
    else: #disjoints et Q < P
        return -1
    
def intersection(n, p,q):
    inter = []
    np = len(p)
    nq = len(q)
    ip = 0 #ind du min des quad de p non exam
    iq = 0 #ind du min des quad de q non exam
    while ip < np and iq < nq:
        c = compare_ccodes(n,p[ip],q[iq])
        if c == 0: # quad egaux
            inter.append(p[ip])
            ip += 1
            iq += 1
        elif c == 2: # p[ip] dans q[iq]
            inter.append(p[ip])
            ip += 1
        elif c == -2: # q[iq] dans p[ip]
            inter.append(q[iq])
            iq += 1
        elif c == 1: # disjoint p[ip] < q[iq]
            ip += 1
        else: #c == -1 disjoints q[iq] < p[ip]
            iq += 1
    return inter
        
    