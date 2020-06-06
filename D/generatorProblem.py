import random


def randomNumber(list1,value2):
    print("Generator",list1)
    n=len(list1)
    output=[]
    list1.sort()
    for i in range(n-1,-1,-1):
        output.append(list1[i])
        if len(output)==value2:
            break

    return output


input1=input("Enter a how many random numbers you want to generate ?")
value=int(input1)
list1=[]

for i in range(value):
    random1=random.randint(500,1000)
    list1.append(random1)

input2=input("how much consuer is accessing ?")
value2=int(input2)

print(randomNumber(list1,value2))