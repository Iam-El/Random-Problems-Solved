def inserionSort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            print("i",i)
            print("j",j)
            nums[j+1]=nums[j]
            print(nums)
            j=j-1
        print("after while",j)
        nums[j+1]=key
        print("nums",nums)
    return nums


nums=[7,8,1,10,3,5]
print(inserionSort(nums))

#
nums = 7,8,1,10,3,5

key = 7

j = 0






