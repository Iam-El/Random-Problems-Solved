
import math

def printPrime(n1,n2):
    output=[]
    def is_prime(num):
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True



    for num in range(n1,n2):
        if is_prime(num):
            output.append(num)




n1=1
n2=10
print(printPrime(n1,n2))