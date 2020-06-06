def commonCharacters(a):
    dict={}
    o=[]
    for i in a:
        for j in i:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] = dict[j] + 1

    for i in dict:
        while dict[i]>=3:
            if dict[i]%3==0:
                o.append(i)
                dict[i]=dict[i]-3

    print(o)




a=["bella","label","roller"]
print(commonCharacters(a))