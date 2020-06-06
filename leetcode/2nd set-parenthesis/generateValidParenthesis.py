def backtrack(str,open,close,n,res):
    if len(str)==2*n:
        res.append(str)
        # print(res)
        print(res)
    else:
        print(open)
        print(close)
        if open<n:
            print("---------1----------")
            print("open",open,"close",close)
            backtrack(str+'(',open+1,close,n,res)
        if close<open:
            print("---------2----------")
            print("open", open, "close", close)
            backtrack(str+')',open,close+1,n,res)


str=''
open=0
close=0
n=3
res=[]
print(backtrack(str,open,close,n,res))