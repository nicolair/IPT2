def k(A,i):
    l = len(A)
    j = i
    nb = 0
    while j < l:
        if A[j] < A[i]:
            nb += 1
        j += 1
    return nb
    
def remplirK(A):
    l = len(A)
    K = []
    for i in range(l):
        K.append(k(A,i))
    return K
    
def PCDC(A):
    l = len(A)
    i = 0
    while i < l-1 and A[i] <= A[i+1]:
        i += 1
    return i

def tribulle(A):
    l = len(A)
    i = PCDC(A)
    while i < l-1:
        A[i] , A[i+1] = A[i+1] , A[i]
        i = PCDC(A)
        
A = [2,4,8,3,7,55,9,12,27]
#tribulle(A)
#print(A)
print(remplirK(A))
        
    