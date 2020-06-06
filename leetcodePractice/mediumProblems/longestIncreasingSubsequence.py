import sys

def longestIncreasingSubsequence(nums):
    n=len(nums)
    dp=[1 for i in range(n)]
    for left in range(1,n):
        for current in range(left):
            if nums[left]>nums[current]:
                dp[left]=max(dp[left],dp[current]+1)

    print(dp)
    maxvalue=-1
    for i in dp:
        if i>=maxvalue:
            maxvalue=i
    print(i)

def findSubsequence(nums):
    n=len(nums)
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            nums[i]=nums[i+1]
            nums.pop(i)
    print(nums)

nums=[10,9,2,5,3,7,101,18]
nums=[10,9,2]
longestIncreasingSubsequence(nums)
