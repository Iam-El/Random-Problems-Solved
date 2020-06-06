def fibo(n):

    if n in memo:
        return memo[n]

    if n==0:
        value=0
    elif n==1:
        value=1
    else:
        value=fibo(n-1)+fibo(n-2)

    memo[n]=value
    return value



memo={}
print(fibo(9))