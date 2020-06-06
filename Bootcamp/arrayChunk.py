def arrayChunk(a,num):
    output=[]
    result=[]
    for i in range(0,len(a),num):
        val=a[i:i+num]
        result.append(val)
    print(result)

a=[1,2,3,4]
a=arrayChunk(a,2)
print(a)