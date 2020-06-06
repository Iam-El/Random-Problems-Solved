def palindromicSubsequence(s):
    n=len(s)

    table=[[1 for i in range(n)]for j in range(n)]

    currentlength=0
    while currentlength<n:
        for i in range(n):
            j=i+currentlength
            if j<n:
                if i==j:
                    table[i][j]=1
                elif i > j:
                    table[i][j] = 1
                elif s[i] == s[j] and currentlength== 1:
                    table[i][j] = 2
                elif s[i]==s[j] and currentlength>=2:
                    max()
                else:
                    table[i][j] = 1
        currentlength=currentlength+1

    for i in range(n):
        print(table[i])




s = "abbcbba"
palindromicSubsequence(s)