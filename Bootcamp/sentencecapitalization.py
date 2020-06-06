def capital(a):
    l=a.split()
    result=[]
    for i in range(len(l)):
        list1=list(l[i])
        val=l[i][0].upper()
        list1[0]=val
        output=''.join(list1)
        result.append(output)
    return ' '.join(result)

a=capital("a short sentence")
print(a)