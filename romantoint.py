def rom(s):
    print(s)
    l = len(s)
    nums = []
    List = list(s)
    print(List)
    for i in range(l):
        if List[i] == 'I':
            nums.append(1)
        elif List[i] == 'V':
            nums.append(5)
        elif List[i] == 'X':
            nums.append(10)
        elif List[i] == 'L':
            nums.append(50)
        elif List[i] == 'C':
            nums.append(100)
        elif List[i] == 'D':
            nums.append(500)
        elif List[i] == 'M':
            nums.append(1000)
    sums = 0
    print(nums)
    for i in range(l - 1):
        if nums[i] >= nums[i + 1]:
            sums += nums[i]
        else:
            sums -= nums[i]
    print(nums[-1])
    sums += nums[-1]
    return sums

a=rom('III')
print(a)