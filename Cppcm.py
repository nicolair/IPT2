def continuer(M):
    p = len(M)
    i = 1
    while i < p and M[i] == M[i-1]:
        i += 1
    return i != p

def indiceMin(M):
    p = len(M)
    iMin = 0
    vMin = M[iMin]
    for i in range(1,p):
        if M[i] < vMin:
            iMin = i
            vMin = M[iMin]
    return iMin
    
def ppcm(A):
    M = []
    for v in A:
        M.append(v)
    while continuer(M):
        iMin = indiceMin(M)
        M[iMin] += A[iMin]
    return M[0]
        
    
lili = [3,5,17,6,4,1]
ppcm(lili)
