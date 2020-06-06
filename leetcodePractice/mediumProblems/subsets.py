# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.

def subsets(nums,index,subarray):
    if index==len(nums):
        print(subarray)
        output.append(subarray)
    else:
        subsets(nums,index+1,subarray)
        subsets(nums,index+1,subarray+[nums[index]])
    return output


output=[]
nums=[1,2,3]
print(subsets(nums,0,[]))