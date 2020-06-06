
intervals=[[1,4],[0,2],[3,5]]


intervals.sort()
print(intervals)
i=0
while i<len(intervals)-1:
    print(len(intervals))
    print(intervals[i])
    output=[]
    if intervals[i][1] >= intervals[i+1][0]:
        first=min(intervals[i][0],intervals[i+1][0])
        second=max(intervals[i][1],intervals[i+1][1])
        intervals.pop(i+1)
        intervals.pop(i)
        output.append(first)
        output.append(second)
        intervals.append(output)
        intervals.sort()
    else:
        i=i+1
print(intervals)