def longestIncreasingSubsequence(nums):
    n=len(nums)
    dp=[1 for i in range (len(nums))]
    for left in range(1,n):
        for current in range(left):
            if nums[left]>nums[current]:
                dp[left]=max(dp[left],dp[current]+1)
    maxvalue=-1
    for i in range(0,len(dp)):
        if dp[i]>maxvalue:
            maxvalue=dp[i]
    return maxvalue


nums=[10,9,2,5,3,7,101,18]
print(longestIncreasingSubsequence(nums))