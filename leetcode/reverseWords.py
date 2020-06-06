# def reverse(str):
#     rev=' '
#     val=str.split()
#     for i in val:
#         if rev=="":
#             rev=i
#         else:
#             rev=i+' '+rev
#     print(rev)


def reverse(str):
    rev=' '
    value=[]
    val=str.split()
    for i in val:
        rev=i+' '+rev
        value.append(i)
    print(' '.join(value))



str="the sky is blue"
reverse(str)

