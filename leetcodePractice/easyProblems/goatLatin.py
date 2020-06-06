def goatLatin(a):
    s=a.split()
    output=[]
    res=[]
    vowel=('a','i','e','o','u','A','I','O','U','E')
    for i in s:
        if i.startswith(vowel):
            output.append(i+'ma')
        else:
            val=i.replace(i[0],"",1)
            output.append(val+i[0]+'ma')
    for j in range(0,len(output)):
        addlatsNumber=('a'*(j+1))
        val=(output[j]+addlatsNumber)
        res.append(val)

    return res
a="I speak Goat Latin"
print(goatLatin(a))