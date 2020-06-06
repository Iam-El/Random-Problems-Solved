
def char(String):
    dict1={}
    flag=True

    for i in range(len(String)):
        if String[i] not in dict1:
            dict1[String[i]]=1
        else:
            dict1[String[i]] =  dict1[String[i]] +1
    print(dict1)

    for j in dict1:
        if dict1[j]>1:
            return True
    return False


String="abdddddcccccd"
a=char(String)
print(a)