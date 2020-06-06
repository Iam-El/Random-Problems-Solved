def validString(s):
    print(s)
    stack=[]
    valid=[]
    count1=0
    count2=0
    for i in range(0,len(s)):
        if s[i]=='(':
            count2=0
            stack.append(s[i])
        if s[i]==')':
            if stack:
                val=stack.pop()
                valid.append(val)
                count2=count2+1
    for i in range(count2):
        valid.append(')')
    print(''.join(valid))


#
# s="((()))"
s=")))((("
validString(s)