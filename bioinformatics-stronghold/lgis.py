

def patience_sort(data):
    piles = []
    last = None
    for d in data:
        if len(piles) == 0:
            t = d, None
            piles.append([t])
            last = t
        else:
            t = d, last
            placed = False
            for i in range(len(piles)):
                if piles[i][len(piles[i])-1][0] < d:
                    piles[i].append(t)
                    placed = True
                    break
            if not placed:
                piles.append([t])

            last = t

    print (piles)

    current = last
    while current[1] is not None:
        print(current[0])
        current = current[1]


seq = [5, 1, 4, 2, 3]

patience_sort(seq)