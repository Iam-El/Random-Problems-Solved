def returnPrimeNumbers(n):
    istrue=True
    for i in range(2,n):
        if n%i==0:
            return 'no prime'
    return 'prime'

n=11
print(returnPrimeNumbers(n))