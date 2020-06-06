def climbstaris(n):
    if n == 0:
        return 1
    elif n==1:
        return 1
    else:
        return climbstaris(n - 1) + climbstaris(n - 2)


n=5
a = climbstaris(n)
print(a)










