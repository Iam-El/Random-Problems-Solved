def vowels(str):
    vowels=['a','e','i','o','u']
    count=0
    lowerstr=(str.lower())
    for i in lowerstr:
        if i in vowels:
            count=count+1
    print(count)


str='Why do you ask?'
print(vowels(str))