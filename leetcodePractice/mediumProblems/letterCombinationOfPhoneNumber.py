def letterCombination(digits):
    arr = [0, 0, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    if digits == "":
        return []
    n = len(digits)
    val1=arr[int(digits[0])]
    print(val1)
    for i in range(1,len(digits)):
        val2=arr[int(digits[i])]
        new_res=[]
        for char in val1:
            for combo in val2:
                new_res.append(char+combo)
        val1=new_res



digits="23"
letterCombination(digits)