def insertionSort1(n, arr):
    a1=[]
    lastelement=arr[len(arr) -1]
    print(lastelement)
    for i in range(n-2,-1,-1):
        if arr[i]<lastelement:
            arr[i+1]=lastelement
            print (' '.join(map(str, arr)))
            break
        else:
            arr[i+1]=arr[i]
            print(' '.join(map(str, arr)))
            if i==0:
                arr[i]=lastelement
                print (' '.join(map(str, arr)))

arr=[2, 3, 4, 5, 6, 7 ,8 ,9, 10, 1]
print(insertionSort1(10,arr))