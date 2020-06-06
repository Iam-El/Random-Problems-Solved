def isBalanced(s):
    stack = []
    l = len(s)
    for i in range(0, l):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            stack.append(s[i])
        if s[i] == ')':
            x = stack.pop()
            print(x)
            if x == '{' or x == '[':
                print('False')
            else:
                print('true')
        elif s[i] == '}':
            x = stack.pop()
            if x == '(' or x == '[':
                print('False')
            else:
                print('True')
        elif s[i] == ']':
            x = stack.pop()
            if x == '{' or x == '(':
                print('False')
            else:
                print('True')

s = '()'
print(s)
isBalanced(s)
