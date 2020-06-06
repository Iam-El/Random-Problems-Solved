import math


def printPrime(n):
    count=0
    list=[2]


    if n<=2:
        return 0

    def isPrime(num):
        for j in range(2,int(math.sqrt(num))+1):
            if num%j==0:
                return False
        return True

    for num in range(3,n):
        if isPrime(num):
            count=count+1
            list.append(num)

    return list

n=10
print(printPrime(n))