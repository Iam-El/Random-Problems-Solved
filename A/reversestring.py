# def recurse(s,res,i,n):
#     if i==n:
#         res=s[i]+res
#         return res
#
#     res=recurse(s,res,i+1,n)
#     res=res+s[i]
#     return res





s="elsy"
res=""
i=0
n=len(s)-1
print(recursion(s,i,n))