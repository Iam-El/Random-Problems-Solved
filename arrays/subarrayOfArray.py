def suarrayfun(arr,index,subarray):



    if index==len(arr):
        print(subarray)
        # if len(subarray)!=0:
        #     print(subarray)
    else:
        suarrayfun(arr,index+1,subarray)
        suarrayfun(arr,index+1,subarray+[arr[index]])




arr=[1,2,3]
list=[]
suarrayfun(arr,0,list)


#subarray (arr,0,[])  -1

#subarray(Arr,1,[])   -2

#subarray(Arr,2,[])   -3

# subarray(Arr,3,[]) -> here print subarray , index=3 , it wont print cos its empty

# goes back to 3 , index=2 , 2+1=3,[]+arr[3]=>[3]


