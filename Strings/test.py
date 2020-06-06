# str1 = "mystring"
# list1 = list(str1)
# print(list1[5])
# list1[5]='u'
# print(list1)
# str1 = ''.join(list1)
# print(str1)


#remove a elements from list . all the occurances

x = [1,2,3,2,2,2,3,4]
print(list(filter(lambda a: a != 2, x)))