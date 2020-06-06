def arrayChunk(a,num):
    output=[]
    result=[]
    i=0
    n=len(a)%num
    print(n)
    while i<len(a):
        output.append(a[i])
        if len(output)==num:
            result.append(output.copy())
            print(result)
            output.clear()
        i=i+1
    if n:
        list1=a[len(a)-n:]
        print(list1)
        result.append(list1)
        print(result)

a=[1,2,3,4,5,6,7,5,6,6]
a=arrayChunk(a,2)
print(a)