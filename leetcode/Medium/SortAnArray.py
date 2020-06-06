# Given an array of integers nums, sort the array in ascending order.
# Merge Sort

def mergeSort(nums):
    mid=len(nums)//2
    if mid==0:
        return nums
    # find left and right

    left=nums[:mid]
    right=nums[mid:]

    #recursive call

    mergeSort(left)
    mergeSort(right)

    # iterators traversing through the two half

    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums[k]=left[i]
            i=i+1
        else:
            nums[k]=right[j]
            j=j+1
        k=k+1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return nums


nums=[5,2,3,1]
print(mergeSort(nums))

print(1+0//2)
