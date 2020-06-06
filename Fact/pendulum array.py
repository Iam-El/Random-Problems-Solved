def pendulumArray(nums):
    res = ['None' for i in range(len(nums))]

    n = len(nums)
    mid = n // 2
    res[mid] = nums[0]
    j = 1

    print("mid",mid)
    for i in range(1, mid + 1):
        res[mid + i] = nums[j]
        j = j + 1
        res[mid - i] = nums[j]
        j = j + 1
        print("i",i)

    if (n % 2) == 0:
        res[mid + i] = nums[j]

    print(res)


nums = [1, 3, 2, 5]
nums.sort()
print(nums)
pendulumArray(nums)
