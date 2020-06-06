def balancedParenthesis(s):
    stack=[]
    isValid=True
    if len(s)==0:
        return True
    elif len(s)==1:
        return False
    else:
        for i in range(0,len(s)):
            if s[i]=='{':
                stack.append('{')
            if s[i] == '[':
                stack.append('[')
            if s[i] == '(':
                stack.append('(')
            if s[i] == '}':
                if stack:
                    if stack[-1]=='}':
                        stack.pop()
                    else:
                        isValid=False
                else:
                    isValid=False
            if s[i] == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        isValid = False
                else:
                    isValid = False
            if s[i] == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        isValid = False
                else:
                    isValid = False
    if len(stack)!=0:
        return False
    if isValid==False:
        return False
    else:
        return True

s="()"
print(balancedParenthesis(s))