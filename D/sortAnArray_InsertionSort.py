def insertionSort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=key
    return nums

nums=[100,1,6,4,5,6,7,8,80]
print(insertionSort(nums))
