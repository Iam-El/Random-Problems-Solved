def generateParenthesis(s,openb,close):
    n=3
    if len(s)==2*n:
        res.append(s)
        return res
    else:
        if openb<n:
             generateParenthesis(s+'(',openb+1,close)
        if close<openb:
             generateParenthesis(s+')',openb,close+1)
    return res

s=''
openb=0
n=3
close=0
res=[]
print(generateParenthesis(s,openb,close))