def getStrength(password, weight_a):
    # Complete the function
    if password is None:
        return 0
    sum = 0
    value = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
        , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict = {}
    for i in value:
        index = value.index(i)
        sum_of_index = index + weight_a
        if sum_of_index > 25:
            sum_of_index = sum_of_index - 26
        dict[i] = sum_of_index

    for letter in password:
        # index_value=value.index(i)
        # sum_of_index=index_value+weight_a
        # if sum_of_index>25:
        #     sum_of_index=sum_of_index-26
        sum = sum + dict[letter]
    return sum