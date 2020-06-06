def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        x=0
        y=1
        sum=0
        for i in range(1,n):
            sum=x+y
            x=y
            y=sum
        print(sum)


fibonacci(9)
