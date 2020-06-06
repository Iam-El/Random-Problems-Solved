def insertionSort(nums):
    for j in range(1,len(nums)):
        key=nums[j]
        i=j-1
        while i>=0 and nums[i]>key:
            nums[i+1]=nums[i]
            i=i-1
        nums[i+1]=key
    return nums


nums=[5,2,3,1]
print(insertionSort(nums))