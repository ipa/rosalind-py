from shared.rosalind import Rosalind

def longsubstr(dnas):
    substr = ''
    if len(dnas) > 1 and len(dnas[0]) > 1:
        for i in range(len(dnas[0])):
            for j in range(len(dnas[0]) -i+1):
                if j > len(substr) and issubstr(dnas[0][i:i+j], dnas):
                    substr = dnas[0][i:i+j]

    return substr

def issubstr(string, dnas):
    if len(dnas) < 1 and len(string) < 1:
        return False
    for i in range(len(dnas)):
        if string not in dnas[i]:
            return False
    return True



dnas = Rosalind.readFasta("input/lcsm.txt")
data = []
for dna in dnas:
    dna.print()
    data.append(dna.dna)


print("result:")
print(longsubstr(data))