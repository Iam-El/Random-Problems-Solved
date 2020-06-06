import math

def closetPoints(points,K):
    dict={}
    origin=[0,0]
    for i in points:
        print(i)
        x=i[0]-origin[0]
        y=i[1]-origin[1]
        eu=math.sqrt(math.pow(x,2)+math.pow(y,2))
        if eu not in dict:
            dict[eu]=[i]
        else:
            currentPoints=dict[eu]
            currentPoints.append(i)
            dict[eu]=currentPoints

    output=[]
    print(dict)
    key=sorted(dict.keys())
    for i in key:
        print(i)
        if len(output)<K:
            print(len(dict[i]))
            output.append(dict[i])
    print(output)




    # print(sortDict)
    # for i in sortDict:
    #     print(i.values())
    # # first2vals = [v for v in sortDict.values()[:2]]
    # # print(first2vals)













points=[[0,1],[1,0]]
K=2
print(closetPoints(points,K))