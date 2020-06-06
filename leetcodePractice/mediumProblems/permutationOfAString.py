def stringPermutation(nums,l,r):

    if l==r:
        temp=[]
        for i in nums:
            temp.append(i)
        result.append(temp)
        print(result)

    for i in range(l,r+1):
        nums[i],nums[l]=nums[l],nums[i]
        stringPermutation(nums,l+1,r)
        nums[i], nums[l] = nums[l], nums[i]


nums=[1,2,3]
result = []
n = len(nums)
stringPermutation(nums,0,n-1)