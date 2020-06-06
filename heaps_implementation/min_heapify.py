def maxheapify(nums, i):
    print(nums)
    left = (2 * i )+ 1

    right = (2 * i) + 2



    if left <=len(nums)-1 and nums[left]<nums[i]:
        largets=left
    else:

        largets=i

    if right<=len(nums)-1 and nums[right]<nums[largets]:
        largets=right


    if largets!=i:

        nums[i],nums[largets]=nums[largets],nums[i]
        maxheapify(nums,largets)

    return (nums)



nums = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
print("nums before",nums)

print(maxheapify(nums,2))
