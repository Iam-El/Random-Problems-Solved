def divisorGame(n):
    if n==0:
        return False
    val=0
    while n>1:
        for x in range(1,n):
            if n%x==0:
                n=n-x
                val=val+1
                break

    if val%2==0:
        return False
    else:
        return True

n=2
print(divisorGame(n))