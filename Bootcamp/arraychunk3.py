def arrayChunk(a,num):
    result=[]

    for i in a:
        last = []
        if last is not None or len(last)==num:
            result.append([i])
        else:
            last.append(i)

    return result

a = [1, 2, 3, 4]
a = arrayChunk(a, 2)
print(a)