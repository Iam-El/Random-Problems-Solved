#Input: points = [[1,3],[-2,2]], K = 1
#Output: [[-2,2]]

import sys
import math

def pointsToOrigin(points,K):
    list1=[]
    origin=[0,0]
    EU=[]
    output=[]
    finalResult=[]
    dictionary={}
    count=0
    for i in points:
        x=i[0]-origin[0]
        y=i[1]-origin[1]
        eu=math.sqrt(math.pow(x,2)+math.pow(y,2))
        if eu not in dictionary:
            dictionary[eu]=[i]
        else:
            currentPoints=dictionary[eu]
            currentPoints.append(i)
            dictionary[eu] = currentPoints
    for key in list(dictionary.keys()):
        output.append(key)
    output.sort()
    print(output)
    print(dictionary)
    for i in output:
        if i in dictionary:
            count=count+1
            finalResult.append(dictionary[i])
            if count==K:
                break
    print(finalResult)




points = [[3,3],[5,-1],[-2,4]]
K = 2
pointsToOrigin(points,K)
