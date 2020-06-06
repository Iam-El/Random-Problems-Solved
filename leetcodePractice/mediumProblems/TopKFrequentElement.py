# Given a non-empty array of integers, return the k most frequent elements.
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

def mostFrequent(nums,k):
    dict={}
    output=[]
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            dict[i] = dict[i] + 1
    values=sorted(dict.values())
    values.reverse()
    resultValue=values[0:k]
    for i in dict:
        if dict[i] in resultValue:
            output.append(i)
    print(output)



nums = [1,2]
k = 2
mostFrequent(nums,k)