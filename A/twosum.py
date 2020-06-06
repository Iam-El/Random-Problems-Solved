# TWO SUM CLOSEST TO K
#Input: nums = [1, 2, 3, 4, 5], target = 10
#Output: [4, 5]

def closest(nums,target):
    nums.sort()
    list1=[]
    result=[0,0]
    i=0
    min_difference=1763173613637613
    j=len(nums)-1
    while i < j:
        difference=target-(nums[i]+nums[j])
        if difference<min_difference:
            min_difference=difference
            result[0]=nums[i]
            result[1]=nums[j]
            i=i+1
        else:
            j=j+1

    print(result)

nums=[1, 2, 3, 4, 5]
target = 10
closest(nums,target)