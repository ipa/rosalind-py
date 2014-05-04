
def ins(unsorted):
    swaps = 0
    for i in range(1, len(unsorted)):
        k = i
        while k > 0 and unsorted[k] < unsorted[k-1]:
            swaps += 1
            t = unsorted[k]
            unsorted[k] = unsorted[k-1]
            unsorted[k-1] = t
            k -= 1
    print(unsorted)
    return swaps


arr = list()
sarr = list()
f = open('input/ins.txt', 'r')
for i, line in enumerate(f):
    if i == 1:
        s = line
        sarr = s.split(' ')
f.close()

for s in sarr:
    arr.append(int(s))

nswaps = ins(arr)
print(nswaps)