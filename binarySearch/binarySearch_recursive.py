def binaryRecursive(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return mid
        elif target<data[mid]:
            return binaryRecursive(data,target,low,mid-1)
        else:
            return binaryRecursive(data,target,mid+1,high)



data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 27
print(binaryRecursive(data,target,0,len(data)-1 ))