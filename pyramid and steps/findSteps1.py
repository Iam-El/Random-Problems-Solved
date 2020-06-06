def findSteps(n):
    for i in range(0,n):
        stairs = ' '
        for j in range(0,n):
            if j<=i:
                stairs=stairs+'#'
            else:
                stairs=stairs+' '
        print(stairs)


findSteps(5)