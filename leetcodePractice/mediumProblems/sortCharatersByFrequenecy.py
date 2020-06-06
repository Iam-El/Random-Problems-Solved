# Given a string, sort it in decreasing order based on the frequency of characters.
# "tree"
# "eert"
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

def sortCharactersByFrequency(s):
    dict={}
    output=[]
    character1=[]
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1
    print(dict)
    valuesSorted=sorted(dict.values())
    valuesSorted.reverse()
    print(valuesSorted)
    for i in valuesSorted:
        print(i)
        for character,frequency in dict.items():
            if i==frequency:
                if character*i not in output:
                    output.append(character*i)
    print(''.join(output))


s="tree"
sortCharactersByFrequency(s)
