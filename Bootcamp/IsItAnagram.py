str1 = "rat bat"
str2 = "car"

dict1 = {}
dict2 = {}
count = 0

isTrue = False

for i in range(len(str1)):
    val1 = str1.count(str1[i])
    dict1.update({str1[i]: val1})
for i in range(len(str2)):
    val2 = str2.count(str2[i])
    dict2.update({str2[i]: val2})
print(dict1)
print(dict2)

for j in dict1:
    if j not in dict2:
        isTrue = False
    elif dict1[j] == dict2[j]:
        isTrue = True
    else:
        isTrue = False
if isTrue == True:
    print("YES")
else:
    print("No")
