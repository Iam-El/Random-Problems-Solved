def tribonacci(n):
    memo={}

    if n in memo:
        return memo[n]

    elif n==0:
        value=0
    elif n==1:
        value=1
    elif n==2:
        value=1
    else:
        value=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

    memo[n]=value
    return value

n=25
a=tribonacci(n)
print(a)