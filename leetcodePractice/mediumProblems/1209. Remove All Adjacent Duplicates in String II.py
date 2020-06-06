# Given a string s, a k duplicate removal consists of
# choosing k adjacent and equal letters from s and removing
# them causing the left and the right side of the deleted substring to concatenate together.

def removeDuplicates(s,k):
    i=0
    count=1
    while i<len(s)-1:
        if s[i]==s[i+1]:
            count=count+1
            if count==k:
                s=s.replace(s[i]*k,"")
                i=0
                count=1
            else:
                i=i+1
        else:
            count=1
            i=i+1
    print(s)


s="abcd"
k=2
removeDuplicates(s,k)
