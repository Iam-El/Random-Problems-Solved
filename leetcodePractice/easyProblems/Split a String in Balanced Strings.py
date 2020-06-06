def splitAString(s):
    count=0
    list=[]
    res=0
    output=[]
    for i in range(0,len(s)):
        if s[i]=='R':
            count=count+1
            list.append(s[i])
        if s[i]=='L':
            count=count-1
            list.append(s[i])
        if count==0:
            res=res+1
            output.append(''.join(list))
            list=[]
    return output


s = "RLLLLRRRLR"
print(splitAString(s))