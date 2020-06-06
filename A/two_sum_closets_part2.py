def closest(nums,target):
    nums.sort()
    list1=[]
    result=[0,0]
    i=0
    min_difference=1763173613637613
    j=len(nums)-1
    while i < j:
        difference=target-(nums[i]+nums[j])
        if difference>0:
            if difference<min_difference:
                min_difference=difference
                result[0]=nums[i]
                result[1]=nums[j]
                i=i+1
        elif difference<0:
            j=j+1
        else:
            print(nums[i-1])
            print(nums[i])
            result[0]=nums[i-1]
            result[1] = nums[j]
            break

    print(result)

nums=[-1, 2, 1, -4]
target = 4
closest(nums,target)