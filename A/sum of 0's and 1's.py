def findSum(nums,left,right):
    while left<=right:
        print("left",left)
        print("right",right)
        mid=(left+right)//2
        print("mid",mid)
        if nums[mid]>nums[mid-1] and nums[mid]==nums[mid+1]:
            return mid
        elif nums[mid]<nums[mid-1] and mid-1!=-1 :
            right=mid-1
        elif nums[mid]<=nums[mid+1] and nums[mid]==0 and mid<len(nums)-1:
            print("here")
            left=mid+1


nums=[0,0,0,0,1]
val=(0+4)//2
print(val)
mid=(findSum(nums,0,len(nums)-1))
print(mid)

sum=0

# for i in range(mid,len(nums)):
#     sum=sum+nums[i]
# print("SUM",sum)