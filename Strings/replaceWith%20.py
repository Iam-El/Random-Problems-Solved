str="Mr John Smith   "
newstr=str.strip()
n=len(newstr)
res=[0]*n
print(res)
for i in range(0,n):
    if ' ' in newstr[i] :
        res[i]='%20'
    else:
        res[i] = newstr[i]
print(''.join(res))
