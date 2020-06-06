def fizbuzz(n):
    output=[]
    for i in range(n):
        if i%3==0 and i%5==0:
            output.append("FizzBuzz")
        elif i%5==0:
            output.append("Fizz")
        else:
            output.append("Buzz")
    print(output)


def fizzbuzzRecursive(a,n):
    if a<n:
        if a%3==0 and a%5==0:
            output.append("Fizzbuzz")
        elif a%5==0:
            output.append("Fizz")
        else:
            output.append("buzz")
        a=a+1
        return fizzbuzzRecursive(a,n)
    else:
        return output

n=100
a=1
output=[]
print(fizzbuzzRecursive(a,n))