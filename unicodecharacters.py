def convertToTitle(n):
    ans = ''
    while n > 0:
        print(n)
        print('here')
        x = n%26
        n = n//26
        if x == 0:
            n -= 1
            ans = 'Z' + ans
        else:
            print(ans)
            ans = chr(x+64) + ans
    return ans

ans=convertToTitle(28)
print(ans)