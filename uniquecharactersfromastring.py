def removeDuplicates(nums):
    list1 = list(nums)
    i = 0
    for j in range(1, len(list1)):
        if list1[j] != list1[i]:
            i = i + 1
            list1[i] = list1[j]
    return i+1

nums = [1,1,2]
a=removeDuplicates(nums)
print(a)
