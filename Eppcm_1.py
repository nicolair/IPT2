def continuer(M):
    p = len(M)
    i = 1
    while i < p and M[i] == M[i-1]:
        i += 1
    return i != p
    
lili = [1,1,1,1,4,1]
print(continuer(lili))
