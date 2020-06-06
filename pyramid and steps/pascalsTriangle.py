def sgenerate(n,res):
    output=[]
    if n==1:
        output.append(1)
        res.append(output)
        print("n:-",n,"output:-",output,"res:-",res)
        return
    else:
        sgenerate(n-1,res)
        if len(res)<2:
            res.append([1,1])
            print("n:-", n, "output:-", output, "res:-", res)
        else:
            val=res[-1]
            o=[]
            for i in range(0, len(val)):
                if i == 0:
                    o.append(val[i])
                else:
                    o.append(val[i - 1] + val[i])
            o.append(1)
            res.append(o)
            return res

res=[]
output=[]
val=sgenerate(6,res)
print(val)