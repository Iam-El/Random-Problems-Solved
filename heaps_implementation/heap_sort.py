def maxheapify(nums, i):
    left = (2 * i) + 1
    right = (2 * i) + 2

    if left <= len(nums) - 1 and nums[left] < nums[i]:
        largets = left
    else:

        largets = i

    if right <= len(nums) - 1 and nums[right] < nums[largets]:
        largets = right

    if largets != i:
        nums[i], nums[largets] = nums[largets], nums[i]
        maxheapify(nums, largets)

    print("nums", nums)
    return (nums)


def buil_a_heap(nums):
    n = len(nums)
    half = n // 2
    for j in range(half, -1, -1):
        maxheapify(nums, j)

    return (nums)


def heap_sort(nums):
    buil_a_heap(nums)
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i], nums[0])
        nums[0], nums[i] = nums[i], nums[0]
        finalnums.append(nums.pop())
        maxheapify(nums, 0)
    return finalnums


finalnums = []
x = [14, 8, 10, 4, 7, 9, 3, 2, 1, 16]
print(heap_sort(x))
