def displayValidOnly(n):
    stack=[]
    stack.append(-1)
    res=0
    for i in range(0,len(s)):
        if s[i]==')':
            stack.append(i)
        else:
            stack.pop()
            if len(stack)==0:
                stack.append(i)
            else:
                res=max(res,i-stack[-1])
    return res



s=")()())"
print(displayValidOnly(s))