
def moveZerosToEnd(nums):
    i=0
    j=0
    count=0
    for i in range(0,len(nums)):
        if nums[i]==0:
            count=count+1
    while j <len(nums):
        if nums[j]==0:
            del nums[j]
        else:
            j=j+1
    i=0
    for i in range(count):
        nums.append(0)
    return (nums)


def deleteMostNumber(nums):
    print(nums)
    j = 0
    while j<len(nums):
        if nums[j]==val:
            del nums[j]

        else:
            j=j+1
    print(nums)


nums=[0,1,0,3,0,0,6,0,12]
nums1=[3,2,2,3]
val=3
print(moveZerosToEnd(nums))
print(deleteMostNumber(nums1))