
def bins(arr, i):
    n = len(arr)
    n2 = int(n/2)

    if n2 == 0 and arr[n2] != i:
        return -1
    elif arr[n2] == i:
        return n2+1
    elif arr[n2] < i:
        r = bins(arr[n2:n], i)
        if r == -1:
            return -1
        else:
            return n2 + r
    else:
        r = bins(arr[0:n2], i)
        if r == -1:
            return -1
        else:
            return r

arr1 = list()
arr2 = list()
sarr1 = list()
sarr2 = list()
f = open('input/bins.txt', 'r')
for i, line in enumerate(f):
    if i == 2:
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

for i in arr2:
    index = bins(arr1, i)
    #print("index of " + str(i) + " is " + str(index))
    print(index, end=" ")
