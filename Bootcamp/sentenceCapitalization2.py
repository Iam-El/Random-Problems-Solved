def capital(a):
    l=a.split()
    words=[]
    for i in range(len(l)):
        val=l[i][0].upper()
        res=val+l[i][1:]
        words.append(res)
    print(' '.join(words))

a=capital("a short sentence")
print(a)