# Brute force # time limited exceeded error

def printPrime(n):
    prime=[]
    count=0
    if n<=2:
        return 0
    for i in range(3,n):
        for j in range(2,i):
            if i%j==0:
                print("i",i)
                prime.append(i)
                count=count+1
                break
        else:
            print("not prime",i)
            print(i)
    print(prime)
    return



n=10
print(printPrime(n))

