def kthLargest(nums,k):
    nums.sort()
    count=0
    i=len(nums)-1
    while i>=0:
        count=count+1
        if count==k:
            return nums[i]
        i=i-1


nums=[3,2,1,5,6,4]
k=2
print(kthLargest(nums,k))