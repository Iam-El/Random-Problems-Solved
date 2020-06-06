def sortAnArray(nums):
    if len(nums)>1:

        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]

        sortAnArray(left)
        sortAnArray(right)

        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
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

nums=[0,0,1,0,2,0,0,1,1,1,2,2,2,2,0,0,0,0,1,1,1,1]
left=0
right=len(nums)
print(sortAnArray(nums))