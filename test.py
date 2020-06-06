
def twoSum( nums, target):
        sum = 0
        output = []
        o = []
        for i in range(0, len(nums)):
            print('Number iiiiiii')
            print(nums[i])
            for j in range(i+1, len(nums)):
                print('nUMBER JJJJJJ')
                print(nums[j])
                sum = nums[i] + nums[j]
                print('summmm')
                print(sum)
                if sum == target:
                    output.append(i)
                    output.append(j)
        o.append(output[0])
        o.append(output[1])
        print(o)

nums=[2,5,5,11]
target=10
twoSum(nums,target)





