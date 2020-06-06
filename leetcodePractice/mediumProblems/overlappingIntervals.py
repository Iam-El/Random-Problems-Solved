def overlappingIntervals(intervals):
    count=0
    i=0
    while i<len(intervals)-1:
        if intervals[i][1]>intervals[i+1][0]:
            count=count+1
            intervals.pop(i+1)
            i=i
        else:
            i=i+1
    return count



intervals=[[1,2],[2,3],[3,4],[1,3]]
print(overlappingIntervals(intervals))