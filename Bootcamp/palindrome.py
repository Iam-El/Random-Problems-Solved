str1="aba"
rev=''
for word in str1:
    rev=word+rev
print(rev)
if rev==str1:
    print("True")
else:
    print("False")