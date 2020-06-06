def maxheapify(nums, i):
    left = (2 * i) + 1

    right = (2 * i) + 2

    if left <= len(nums) - 1 and nums[left] > nums[i]:
        largets = left
    else:

        largets = i

    if right <= len(nums) - 1 and nums[right] > nums[largets]:
        largets = right

    if largets != i:
        nums[i], nums[largets] = nums[largets], nums[i]
        maxheapify(nums, largets)

    return (nums)


def buil_a_heap(nums):
    n = len(nums)
    half = n // 2
    for i in range(half, -1, -1):
        maxheapify(nums, i)

    return (nums)


def extract_max(nums):
    if len(nums) == 0:
        return None
    largest = nums[0]
    nums[0] = nums[-1]
    del nums[-1]
    if len(nums) > 1:
        maxheapify(nums,0)
    return largest


nums = [5, 3,17, 10, 84, 19, 6, 22, 9]



print(buil_a_heap(nums))

# print(extract_max(nums))

k=3
count=0
while count<k:
    print(extract_max(nums))
    count=count+1
