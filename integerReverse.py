def reverse(x):
    print(x)
    rev = 0
    while x<0:
        print(x)
        print('here')
        sign = -1
        x = x * sign
        rev = (10 * rev) + x % 10
        x //= 10
        rev = -rev
    return rev
    # while x > 0:
    #     rev = (10 * rev) + x % 10
    #     x //= 10
    # return rev
print(reverse(-123))