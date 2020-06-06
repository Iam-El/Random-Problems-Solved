import math

def printPrime(n):


    if n<=2:
        return 0

    output = []

    def is_Prime(num):
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True


    for num in range(2,n):
        if is_Prime(num):
            output.append(num)
    return output


n=10
print(printPrime(n))










n=10
printPrime(n)