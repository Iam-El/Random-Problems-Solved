def findSteps(n,i):
    if n<1:
        return
    if i <= n:
        print("* ", end=' ')
        findSteps(n, i +1)
    else:
        print("")
        findSteps(n-1,1)

stairs=' '
i=1
findSteps(5,i)
