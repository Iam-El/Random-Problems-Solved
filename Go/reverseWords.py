def reversWords(string):
    rev=" "
    stringSplit=string.split()
    for i in stringSplit:
        if rev==" ":
            rev=i
        else:
            rev=i+" "+rev
    print(rev)


string="elsy is words"
reversWords(string)







