

def maj(arr):
    arr.sort()
    n = len(arr)
    n2 = int(round(n/2, 0))

    counter = 0
    lasti = arr[0]
    for i in arr[1:n]:
        if i == lasti:
            counter += 1
            if counter >= n2:
                return i
        else:
            counter = 0
            lasti = i
    return -1


maj_arr = list()
f = open('input/maj.txt', 'r')
for i, line in enumerate(f):
    if i > 0:
        s = line
        sarr = s.split(' ')
        iarr = list()
        for s in sarr:
            iarr.append(int(s))
        maj_arr.append(iarr)

for arr in maj_arr:
    m = maj(arr)
    print(m, end=" ")