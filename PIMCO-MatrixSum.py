




def sumOfCoulumn(numRows,numCol,a):
    for i in range(numRows):
        for j in range(1,numCol):
            a[i][j]=a[i][j]+a[i][j-1]
            print("column",a)


def sumOfRows(numRows,numCol,a):
    for i in range(1,numRows):
        for j in range(numCol):
            a[i][j]=a[i][j]+a[i-1][j]
            print(a)


a = [[3, 7, 1], [2, 4, 0], [9, 4, 2]]
numRows = len(a)
numCol = len(a[0])
sumOfCoulumn(numRows,numCol,a)
sumOfRows(numRows,numCol,a)
print(a)