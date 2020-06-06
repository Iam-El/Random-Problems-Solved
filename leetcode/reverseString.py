def reverse(str):
    rev=""
    for i in str:
        rev=i+rev
    print(rev)

str="elsy"
reverse(str)