

def inv(unsorted):
    n = len(unsorted)
    counter = 0
    for i, sub in enumerate(unsorted):
        actual = unsorted[i]
        for compare in unsorted[i:n]:
            if compare < actual:
                    counter += 1
    return counter

unsorted_list = list()
f = open('input/inv.txt', 'r')
for i, line in enumerate(f):
    if i == 1:
        arr = line.split(' ')
        for s in arr:
            unsorted_list.append(int(s))

inversions = inv(unsorted_list)
print(inversions)