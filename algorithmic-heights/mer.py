__author__ = 'Iwan'

def mer(arr1, arr2):
    n = len(arr1) + len(arr2)
    i1 = 0
    i2 = 0
    narr = list()

    for i in range(0, n):
        if i1 >= len(arr1) and i2 <= len(arr2):
            narr.append(arr2[i2])
            i2 += 1
        elif i1 <= len(arr1) and i2 >= len(arr2):
            narr.append(arr1[i1])
            i1 += 1
        elif arr1[i1] < arr2[i2]:
            narr.append(arr1[i1])
            i1 += 1
        else:
            narr.append(arr2[i2])
            i2 += 1

    return narr


arr1 = list()
arr2 = list()
sarr1 = list()
sarr2 = list()
f = open('input/mer.txt', 'r')
for i, line in enumerate(f):
    if i == 1:
        s = line
        sarr1 = s.split(' ')
    if i == 3:
        s = line
        sarr2 = s.split(' ')
f.close()

for s in sarr1:
    arr1.append(int(s))
for s in sarr2:
    arr2.append(int(s))

print(arr1)
print(arr2)

new = mer(arr1, arr2)
for num in new:
    print(num, end=' ')