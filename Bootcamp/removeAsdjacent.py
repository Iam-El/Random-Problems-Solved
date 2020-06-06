def adjacentduplicate(s,k):
    count=1
    i=0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            count=count+1
            if count==k:
                s=s.replace(s[i]*k,"")
                count=1
                i=0
            else:
                i=i+1
        else:
            count=1
            i=i+1
    return s
a=adjacentduplicate("deeedbbcccbdaa",3)
print("return value",a)

#ddbbcccbdaa
