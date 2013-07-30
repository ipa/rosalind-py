
def factorial (n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def permutations(elements):
    if len(elements) <=1:
        yield elements
    else:
        for permutation in permutations(elements[1:]):
            for i in range(len(elements)):
                yield permutation[:i] + elements[0:1] + permutation[i:]

n = 5
digits = []
for i in range(n):
    digits.append(i+1)

f = open('perm_output.txt', 'w')
print(factorial(n))
f.write(str(factorial(n)))
myperms = permutations(digits)


for i in myperms:
    print(str(i))
    f.write(str(i))
    f.write("\n")
    #i[0], i[1], i[2], i[3], i[4], i[5], i[6]
f.close()