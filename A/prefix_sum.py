arr = [ -2, -3, 4, -1, -2, 1, 5, -3 ]

n1 = len(arr)
prefix_sum = []
prefix_sum.append(arr[0])
min_prefix_sum=0
res=-11244444438834374
for i in range(1, n1):
        prefix_sum.append(prefix_sum[i - 1] + arr[i])

print(prefix_sum)
for i in range(n1):
    res = max(res, prefix_sum[i] - min_prefix_sum)
    min_prefix_sum=min(min_prefix_sum, prefix_sum[i])
print(res)
