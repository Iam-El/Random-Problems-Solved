# id=[0]
#
# id[0]+=1
# print(id)
#
# print(5//2)

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2, seq)
print(list(result))

# result contains even numbers of the list
result1 = filter(lambda x: x % 2 == 0, seq)
print(list(result1))


str="ABAB"
k=2
for i in range(0,len(str),k):
    val1=(str[i:k])
    print(i,"-----",val1)
    str=str.replace(val1,"",1)
    print(str)

    # print(str[i:k])

# str2="ABAB"
# for i in range(0,len(str2),k):
#     print("i",i)
#     val1=str2[i:k]
#     print(str2[i:k])
#     print("str2",val1)

a=[1]
print(a[0:])


print(5//2)