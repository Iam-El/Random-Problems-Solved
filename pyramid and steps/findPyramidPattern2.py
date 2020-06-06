def print_space(space):
    if space==0:
        return
    print(" ",end=' ')
    print_space(space-1)

def print_asterick(asterick):
    if asterick==0:
        return
    print("#",end=' ')
    print_asterick(asterick-1)


def findPyramid(n,i,j):
    if n<1:
        return
    print_space(n-1)
    print_asterick((i-n+1)+j)
    print(" ")
    j=j+1
    findPyramid(n-1,5,j)


i=5
j=0
findPyramid(5,i,j)