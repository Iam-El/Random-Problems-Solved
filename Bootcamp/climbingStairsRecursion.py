def recursion(n):
    if n==1:
        return '#'
    else:
        return ( '#'+recursion(n-1))

a=recursion(10)
print(a)
