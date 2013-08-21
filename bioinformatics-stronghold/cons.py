from shared.rosalind import Rosalind




profile = ['A', 'C', 'G', 'T']
dnas = Rosalind.readFasta("input/cons.txt")

m = len(dnas)
n = len(dnas[0].dna)

P = [[0 for x in range(n)] for x in range(m)]
cons = [[0 for x in range(n)] for x in range(4)]

for i in range(m):
    for j in range(n):
        P[i][j] = dnas[i].dna[j]
        c = P[i][j]
        if c == 'A':
            cons[0][j] += 1
        elif c == 'C':
            cons[1][j] += 1
        elif c == 'G':
            cons[2][j] += 1
        elif c == 'T':
            cons[3][j] += 1

# Print

columns = zip(*cons)

for column in columns:
    maxValIndex = column.index(max(column))
    print(profile[maxValIndex], end="")

print('')
for i in range(4):
    if i == 0:
        print('A: ', end="")
    elif i == 1:
        print('C: ', end="")
    elif i == 2:
        print('G: ', end="")
    elif i == 3:
        print('T: ', end="")
    for j in range(n):
        print(cons[i][j], ' ', end="")

    print('')

# print(cons)