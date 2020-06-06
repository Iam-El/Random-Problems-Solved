def stringToInter(num):
    if num<0:
        isNegative=True
        num =(num)*(-1)
        print(num)
    else:
        isNegative=False
    output=[]

    while num>0:

        lastNum=num%10
        print(lastNum)
        print("------------",chr(ord('0')+lastNum))
        output.append(chr(ord('0')+lastNum))
        print(output)
        num=num//10
    output=(output[::-1])

    if isNegative:
        print('-'+''.join(output))
    else:
        print(''.join(output))

print("bllll")

nums=[1,2,3,4]
for i ,v in enumerate(nums):
    print(i,v)

num=-123
stringToInter(num)