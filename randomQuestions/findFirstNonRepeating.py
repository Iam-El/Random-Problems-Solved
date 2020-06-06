def firstNonRepeating(a):
    d={}
    for i in range(0,len(a)):
        if a[i] not in d:
            d[a[i]]=1
        else:
            d[a[i]]=d[a[i]]+1
    for i in a:
        if d[i]==1:
            return i

a='ssaabbcccdddde'
print(firstNonRepeating(a))