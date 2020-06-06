# dictionary = [0, 0, 0];
#         dictionary = {}
#         if n<=2:
#             return 0
#         count = n-1
#         for num in range(2,n):
#             if num==2:
#                 count=count-1
#             print(dictionary, num)
#             for j in range(2,num):
#                 if dictionary.has_key(j) and dictionary[j]:
#                     count = count-1
#                 elif num%j==0:
#                     count = count-1
#                     dictionary[j] = True
#                     break

#         return count


# class Solution(object):
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         self.dictionary = [0, 0]
#         return self.isPrime(n)
#
#     def isPrime(self, n):
#         # print(n)
#         if n <= 1:
#             return self.dictionary[n];
#         # if len(self.dictionary:
#         #     return self.dictionary[n]
#         isPrimeBool = True;
#         for j in range(2, n):
#             if n % j == 0:
#                 isPrimeBool = False
#                 break
#         if isPrimeBool:
#             print(n)
#             return self.isPrime(n - 1) + 1
#         return self.isPrime(n - 1)



# d=[[1],[1,1]]
# val=d[-1]
# print(val)
# o=[]
# for i in range(0,len(val)):
#     if i==0:
#         o.append(val[i])
#     else:
#         o.append(val[i-1]+val[i])
# o.append(1)
# print(o)
# d.append(o)
# print(d)



# def prepend(List, str):
#     # Using format()
#     str += '{0}'
#     List = ((map(str.format, List)))
#     return List
#
#
# # Driver function
# list = [1, 2, 3, 4]
# str = 'Geek'
# print(prepend(list, str))
#
# l = [1, 2, 3, 4]
# print(l[:-1])
# print(l[::-1])

# print(list("Hello"))
#
# s="elsy"
# print(s[:-1])
#
#
# print(chr(ord('0')+20))
# helloWorld = "Hello World!"
# print(len(helloWorld))
# hellWrld = helloWorld.replace("o","")
# print(len(hellWrld))
# #

# L = [[1,2,3],[4,5,6],[7,8,9]]
# print(L[::-1])
#
# print(6//2)
# interval=1
# for i in range(0,3-interval):
#     print(i)
#     interval=interval*2

# dict1={}
# print(dict1)
#
# dict1['email']={}
# print(dict1)
#
# dict1['email']['firtstname']='elsy'
# dict1['email']['lastname']='fernandes'
# print(dict1['email'])
#
#
# print(5//2)

#
# list1=['let1 art cn', 'let2 own kit dig', 'let3 art aero']
#
# list2=sorted(list1)
# print(list2)
# #


# OrderedDict([('dig1 8 1 5 1', 'dig1 8 1 5 1'), ('dig2 3 6', 'dig2 3 6')])
# ['let1 art cn', 'let2 own kit dig', 'let3 art aero']
# let1 art cn
# let2 own kit dig
# let3 art aero
# list1=[1,2,3,4,6,8]
# n=len(list1)
# print("n",n)
# l1=n-2
# print(l1)
# l2=n-3
# print(l2)
# print((2+3)/2)





# print(chr(ord('0')))

value2=(ord(chr(4)))
print(type(value2))

value=(chr(ord('0')+5))
print(type(value))


