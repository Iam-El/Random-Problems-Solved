def pendulumArrangement(arr, n):
    n = len(arr)
    arr.sort()
    op = [0] * n
    mid = (n // 2)
    print(mid)
    j = 1
    i = 1
    op[mid] = arr[0]
    for i in range(1, mid + 1):
        print(i)
        op[mid + i] = arr[j]
        j += 1
        op[mid - i] = arr[j]
        j += 1
    print(arr)

    if (int(n % 2) == 0):
        op[mid + i] = arr[j]


arr = [14, 6, 19, 21]
n = len(arr)
pendulumArrangement(arr, n)
