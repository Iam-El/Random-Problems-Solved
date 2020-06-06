def findPalindrome(arr):
    palindrome=[]
    for i in arr:
        rev=''
        for j in i:
            rev=j+rev
        if rev==i:
            palindrome.append(rev)

    print(palindrome)
    for i in range(0,len(palindrome)):
        if len(palindrome[i])==3:
            return palindrome[i]

arr=['anna','tech','vaccur','civic','pop']
print(findPalindrome(arr))