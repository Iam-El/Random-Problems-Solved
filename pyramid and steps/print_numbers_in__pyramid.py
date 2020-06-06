def findSteps(n,i):
    if n<1:
        return
    if i>= n:
        print(n, end=' ')
        findSteps(n,i - 1)

    else:
        print("")
        findSteps(n-1,5)

stairs=' '
i=5
findSteps(5,i)
