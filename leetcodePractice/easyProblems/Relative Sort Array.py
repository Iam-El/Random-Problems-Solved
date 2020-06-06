def relativeSortAnArray(arr1,arr2):
    ans=[]
    dict={}
    for i in arr1:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1
    for i in arr2:
        if i in dict:
           ans=ans+[i]*dict[i]
        else:
            ans.append(i)
    for j in dict:
        if j not in arr2:
            ans.append(j)
    print(ans)


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
relativeSortAnArray(arr1,arr2)

[2,2,2,1,4,3,3,9,6,7,19]