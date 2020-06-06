s = "HELLO"
for i in range(0,len(s)-1):
    s=s[-1]+s[:-1]
    print(s)
