

def patience_sort_decreasing(data):
    piles = []
    last = None
    for d in data:
        if len(piles) == 0:
            t = d, None
            piles.append([t])
            last = t
        else:

            placed = False
            for i in range(len(piles)):
                if piles[i][len(piles[i])-1][0] < d:
                    t = d, len(piles[i-1])-1
                    piles[i].append(t)
                    placed = True
                    break
            if not placed:
                t = d, len(piles[len(piles)-1])-1
                piles.append([t])

    return piles

def patience_sort_increasing(data):
    piles = []
    last = None
    for d in data:
        if len(piles) == 0:
            t = d, None
            piles.append([t])
            last = t
        else:

            placed = False
            for i in range(len(piles)):
                if piles[i][len(piles[i])-1][0] > d:
                    t = d, len(piles[i-1])-1
                    piles[i].append(t)
                    placed = True
                    break
            if not placed:
                t = d, len(piles[len(piles)-1])-1
                piles.append([t])

    return piles


def print_sequence(piles):
    i = 1
    current_pile = piles[len(piles)-i]
    backpointer = current_pile[len(current_pile)-1][1]
    current = current_pile[len(current_pile)-1]

    longest_increasing = []

    while i <= len(piles):
       #print(current)
       i += 1
       longest_increasing.append(current[0])
       if backpointer is None or i > len(piles):
           break
       current_pile = piles[len(piles)-i]
       current = current_pile[backpointer]
       backpointer = current[1]

    for x in reversed(longest_increasing):
        print(x, end=" ")

seq = []

file = open('input/lgis.txt', 'r')
for line in file:
    arr = line.split(' ')
    for a in arr:
        seq.append(int(a))

#seq = [5, 1, 4, 2, 3]
#print('increasing')
print_sequence(patience_sort_increasing(seq))
print(' ')
#print('decreasing')
print_sequence(patience_sort_decreasing(seq))
#print(piles)
