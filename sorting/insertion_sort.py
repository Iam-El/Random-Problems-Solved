
def insertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        print("start key", key)
        j=i-1
        while j>=0 and a[j]>key:
            print("keyyyyy",key)
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
        print("key",key)
        print(a)
        print("--------------")
    return a

a=[5,2,4,6,1,3]
val=insertionSort(a)
print(val)


