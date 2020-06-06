import math


# def printAllPrime(n):
#     isprime=[2]
#     if n<=2:
#         return 0
#     max_divisor=int(math.sqrt(n))
#     print(max_divisor)
#     for i in range(3,n):
#         print("i",i)
#         for j in range(2,max_divisor+1):
#             if i%j==0:
#                 break
#         else:
#             isprime.append(i)
#     print(isprime)
#
#
# n=20
# print(printAllPrime(n))

def primeTest(num):
    output=[]
    def is_prime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2,n):
        if is_prime(num):
            output.append(num)


    return len(output)

n=10
print(primeTest(n))