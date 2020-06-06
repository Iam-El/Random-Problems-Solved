def testFunction(a,b,output):
    if (a<=b):
        if a%3==0 and a%5==0:
            output.append("LUTRON")
        elif a%5==0:
            output.append('TRON')
        elif a%3==0:
            output.append('LU')
        else:
            output.append(a)
        a=a+1
        return testFunction(a,b,output)
    else:
        return output

n=100
output=[]
print(testFunction(1,n,output))



