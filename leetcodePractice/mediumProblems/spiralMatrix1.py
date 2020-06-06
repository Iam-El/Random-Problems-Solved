def spiralMatrix(matrix):
    if len(matrix)==0:
        return []
    output=[]
    res=[]
    startRow=0
    startColumn=0
    endRow=len(matrix)-1
    endColumn=len(matrix[0])-1
    while startRow<=endRow and startColumn<=endColumn:
        i=startColumn
        while i<=endColumn:
            output.append(matrix[startRow][i])
            i=i+1
        startRow=startRow+1
        i=startRow
        while i<=endRow:
            output.append(matrix[i][endColumn])
            i=i+1
        endColumn=endColumn-1
        i=endColumn
        while i>=startColumn:
            output.append(matrix[endRow][i])
            i=i-1
        endRow=endRow-1
        i=endRow
        while i>=startRow:
            output.append(matrix[i][startColumn])
            i=i-1
        startColumn=startColumn+1
        i=startColumn
    print(output)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))