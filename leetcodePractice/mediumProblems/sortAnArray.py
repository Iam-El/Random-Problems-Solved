def mergerSort(nums):
    mid=len(nums)//2
    if mid==0:
        return nums
    left=nums[:mid]
    right=nums[mid:]

    mergerSort(left)
    mergerSort(right)


    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):
        print(left)
        print(right)
        if left[i]< right[j]:
            nums[k]=left[i]
            i=i+1
            k=k+1
        else:
            nums[k]=right[j]
            j=j+1
            k=k+1

    while i<len(left):
        nums[k]=left[i]
        i=i+1
        k=k+1

    while j<len(right):
        nums[k]=right[j]
        j=j+1
        k=k+1

    return nums


nums=[6,7,5,1,4,7,8,9,2]
if len(nums)>0:
    print(mergerSort(nums))
else:
    print(nums)
