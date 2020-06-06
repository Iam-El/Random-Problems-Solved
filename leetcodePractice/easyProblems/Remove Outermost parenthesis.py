def removeOuterParenthesis(s):
    count1=0
    count2=0
    val=[]
    res=''
    for i in range(0,len(s)):
        if s[i]==')':
            count1=count1+1
            val.append(s[i])
        if s[i]=='(':
            count2=count2+1
            val.append(s[i])
        if count1==count2:
            val=val[1:-1]
            res=res+''.join(val)
            count1 = 0
            count2 = 0
            val=[]
    return res


s='()()'
print(removeOuterParenthesis(s))