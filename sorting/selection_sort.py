def selectionSort(a):
    for i in range(0,len(a)):
        min_idx=i
        for j in range(i+1,len(a)):
            if a[j]<a[min_idx]:
                min_idx=j
                temp=a[min_idx]
                a[min_idx]=a[i]
                a[i]=temp
    return a


a=[5,3,1,8,9, 10,1]
val=selectionSort(a)
print(val)