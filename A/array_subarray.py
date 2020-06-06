def subArray(num1,num2):
    n=len(num1)
    for i in range(len(num2)):
        value=num2[i:n]
        n=n+1
        print(num1)
        print(value)
        print("--------")
        if num1==value:
            return True
    return False

def twopointer(num1,num2):
    i=0
    j=0
    count=0
    while i<len(num1) and j <len(num2):
        if num1[i]==num2[j]:
            count=count+1
            print(count)
            i=i+1
            j=j+1
        else:
            j=j+1

        if count==len(num1):
            return True
    return False

num1=[3,0,19,1]
num2=[2,3,0,5,1,1,2]
print(twopointer(num1,num2))





[1,2,3,4,5,6,7,8,9]


