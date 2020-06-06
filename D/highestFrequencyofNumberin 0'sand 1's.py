def highestFrequencyNumber(nums):
    dict={}
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            dict[i] = dict[i] + 1
    print(dict)

    max=0
    for i in dict:
        if dict[i]>max:
            max=dict[i]
    return max

s="000010101000011111100"
print(highestFrequencyNumber(s))