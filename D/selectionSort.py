def selectionSort(nums):

    for i in range(0,len(nums)):
        for k in range(i+1,len(nums)):
            if nums[k]<nums[i]:
                temp=nums[i]
                nums[i]=nums[k]
                nums[k]=temp
    return nums


nums = [100, 1, 6, 4, 5, 6, 7, 8, 80]
print(selectionSort(nums))

