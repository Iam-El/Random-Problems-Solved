def binarySearch(nums,target):

    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1


def recursiveBibarySearch(nums,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            return recursiveBibarySearch(nums,target,low,mid-1)
        elif target>nums[mid]:
            return recursiveBibarySearch(nums,target,low+1,high)


def newPracticeBinary(nums,target):
    left=0
    right=len(nums)-1
    print(nums)
    print(target)
    while left<=right:
        mid=(left+right)//2
        print("nums",nums[mid])
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            print("here1")
            right=mid-1
        else:
            print("here2")
            left=mid+1


def nePracticeRecursive(nums,target,left,right):
    if left>right:
        return False
    else:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return nePracticeRecursive(nums,target,mid+1,right)
        else:
            return nePracticeRecursive(nums,target,left,mid-1)



data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target=27
# print(newPracticeBinary(data,target))
#
low=0
high=len(data)-1
print(nePracticeRecursive(data,target,low,high))