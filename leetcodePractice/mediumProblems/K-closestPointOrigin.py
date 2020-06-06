import math

def pointsToOrigin(points,K):

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
    print(dictionary)
    keys=sorted(dictionary.keys())
    print(keys)
    for i in keys:
        currentOutput=len(output)
        if (currentOutput)<K:
            print(len(dictionary[i]))
            if len(dictionary[i])<K-currentOutput:
                for x in dictionary[i]:
                    output.append(x)
            else:
                for x in dictionary[i]:
                    output.append(x)
    print(output)


# points = [[3,3],[5,-1],[-2,4]]
points=[[1,0],[0,1]]
K = 2
pointsToOrigin(points,K)
