# input 2, 16,10
# output 16 11 6 1 -4 1 6 11 16
# output 10 5 0 5 10



def printN(n):
    print(n ,end=" ")
    if n<=0:
        return
    printN(n-5)
    print(n ,end=" ")


printN(10)
