def bigSorting(unsorted):
    for i in range(0, len(unsorted)):
        unsorted[i] = int(unsorted[i])
    l = len(unsorted)
    for i in range(l):
        min_idx = i
        for j in range(i + 1, l):
            if unsorted[j] < unsorted[min_idx]:
                min_idx = j
        temp = unsorted[i]
        unsorted[i] = unsorted[min_idx]
        unsorted[min_idx] = temp

    return unsorted


print(bigSorting(['6','31415926535897932384626433832795','1','3','10','3','5']))