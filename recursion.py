def recursion(num,string):
    if num==1:
        return 1
    string=num*string
    string=recursion(num-1,string)
    return string

num=3
string=""
print(recursion(num,string))

