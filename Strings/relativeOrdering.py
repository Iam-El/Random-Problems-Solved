def relativeorder(arr1,arr2):
    list2=[]
    data={}
    ans=[]
    for num1 in arr1:
        if num1 not in arr2:
            list2.append(num1)
        if num1 in arr2:
            count=arr1.count(num1)
            data.update({num1:count})
    print(data)
    for num2 in arr2:
        ans=ans+[num2]*data[num2]
    print(ans+list2)


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
relativeorder(arr1,arr2)


