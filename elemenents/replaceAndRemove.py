#  Replace each'a'by two'd's.
# Delete each entry containing a'b'.
#y (d,d,c,d,c,d,d).
a=['a','c','d','b','b','c','a']


count=0
i=0
while i<len(a):
    if a[i]=='a':
        a.pop(i)
        a.insert(i,'d')
        a.insert(i,'d')
        i=0
    if a[i]=='b':
        print(a[i])
        a.remove(a[i])
        i=0
    i=i+1
print(a)




