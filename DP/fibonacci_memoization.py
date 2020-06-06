fibonacci_catche={}  # create a dictinary to store the value

def fib(n):

    # if u have catched the value then return it

    if n in fibonacci_catche:
        return fibonacci_catche[n]


    # else compute the nth term
    if n==1:
        value=1
    elif n==2:
        value=1
    elif n>2:
        value=fib(n-1)+fib(n-2)

    #catche it and return it

    fibonacci_catche[n]=value
    return value


for n in range(1,1000):
    print(n,":",fib(n))
