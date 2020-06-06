def reverse_integer(x):
    if x < 0:
        sign = -1
    else:
        sign = 1
    x=x*sign

    # Remove leading zero in the reversed integer
    while x:
        if x % 10 == 0:
            x /= 10
        else:
            break

    # string manipulation
    x = str(x)
    lst = list(x)  # list('234') returns ['2', '3', '4']
    lst.reverse()
    x = "".join(lst)
    x = int(x)
    return sign * x


print(reverse_integer(1534236469))
print(reverse_integer(-123))