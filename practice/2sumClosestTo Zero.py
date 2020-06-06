def minAbsSumPair(nums):
    target=0
    n=len(nums)
    value1=0
    value2=0
    maxdifference=24242424242424
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            difference=abs(sum)-target
            if difference<maxdifference:
                maxdifference=difference
                value1=nums[i]
                value2=nums[j]
    print(maxdifference)
    print(value1)
    print(value2)

nums = [1, 60, -10, 70, -80, 85,-81,84]
minAbsSumPair(nums)