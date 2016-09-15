R0 = [[1,2],[2,7],[0,2],[9,0],[8,1],
    [2,3],[7,4],[7,6],[5,6],[7,5],[5,9]]

n = 10
r = [[False for i in range(n)] for j in range(n)]
for p in R0:
    r[p[0]][p[1]] = True
print(r)

T = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            T.append([i,j,k])

pasTrans = True
while pasTrans:
    pasTrans = False
    for t in T:
        if r[t[0]][t[1]] and r[t[1]][t[2]]
                         and not r[t[0]][t[2]]:
            pasTrans = True
            r[t[0]][t[2]] = True
            
print(r)
