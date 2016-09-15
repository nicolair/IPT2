n = 10000
notes = []
freq = [0 for i in range(20)]
for i in range(n):
    notes.append(randint(0,200)/10.)

notes[5] = 20.
notes[6] = 0.
#print(notes)
#print(freq)

for nono in notes:
    v = 0
    while v < nono :
        v += 1
    freq[v -1] += 1
    
print(freq)
s = 0
for f in freq:
    s += f
print(s)