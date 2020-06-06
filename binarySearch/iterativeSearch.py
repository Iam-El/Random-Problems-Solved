def iteraiveSearch(data,target):
    for i in range(0,len(data)):
        if target==data[i]:
            return i


data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 27
print(iteraiveSearch(data,target))