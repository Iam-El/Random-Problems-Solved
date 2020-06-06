def reverse(num,rev):
    if num==0:
        return rev

    rem=num%10
    rev=rem+rev*10
    num=num//10
    return reverse(num,rev)



num=123
rev=0
print(reverse(num,rev))
