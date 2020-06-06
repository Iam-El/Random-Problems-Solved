String="abccccccccccd"

dict={}

for i in range(0,len(String)):
    if String[i] not in dict:
        dict[String[i]]=1
    else:
        dict[String[i]] = dict[String[i]]+1
    # val=String.count(String[i])
    #
    # dict.update({String[i]:val})
print(dict)
currentMax = 0
currentMaxChar = ''
for j in dict:
    if dict[j] > currentMax:
        currentMax = dict[j]
        currentMaxChar = j

print(currentMaxChar)

