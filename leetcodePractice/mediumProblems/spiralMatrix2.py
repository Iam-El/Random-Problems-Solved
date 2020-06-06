#Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

def spiralMatrix2(n):
    output=[[0 for i in range(n)]for j in range(n)]
    print(output)
    startRow=0
    startColumn=0
    endRow=len(output)-1
    endColumn=len(output[0])-1
    val=1
    if n==1:
        return [[val]]
    while startRow<=endRow and startColumn<=endColumn:
        i=startColumn
        while i<=endColumn:
            output[startRow][i]=val
            val=val+1
            i=i+1
        startRow=startRow+1
        i=startRow
        while i<=endRow:
            output[i][endColumn]=val
            val=val+1
            i=i+1
        endColumn=endColumn-1
        i=endColumn
        while i>=startColumn:
            output[endRow][i]=val
            val=val+1
            i=i-1
        endRow=endRow-1
        i=endRow
        while i>=startRow:
            output[i][startColumn]=val
            val=val+1
            i=i-1
    print(output)















n=3
print(spiralMatrix2(n))