nmax = 4
CoeffBin = (nmax + 1)*[0]
#initialisé comme une liste de 0
for n in range(nmax + 1):
  CoeffBin[n] = (n+1)*[1]
  #initialisé comme une liste de 1
  for p  in range(n-1):
    CoeffBin[n][p+1] = CoeffBin[n-1][p+1] + CoeffBin[n-1][p]  
print(CoeffBin)
