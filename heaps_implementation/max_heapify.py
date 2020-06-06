def max_heapify(nums, i):
    left = (2 * i) + 1
    right = (2 * i) + 2

    if left <= len(nums) - 1 and nums[left] < nums[i]:
        largest = left
    else:
        largest = i

    if right <= len(nums) - 1 and nums[right] <largest:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums,largest)
    print(nums)


def buildAheap(nums):
    a=len(nums)
    half=a//2
    for i in range(half,-1,-1):
        max_heapify(nums,i)
    return (nums)

nums=[15, 11, 14, 9, 10, 13, 3, 8, 4, 2, 5, 12, 6, 1, 7]
i=0
print(buildAheap(nums))