def removeDuplicates(nums):
    list1 = list(nums)
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i = i + 1
            nums[i] = nums[j]
    print(i+1)

nums = [1, 1, 2]
removeDuplicates(nums)
