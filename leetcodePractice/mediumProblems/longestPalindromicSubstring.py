def palindromicSubstring(s):
    n = len(s)
    table = [[False for i in range(n)] for j in range(n)]

    current_length = 0
    max_sequence = 1
    max_seq_i = 1
    max_seg_j = 1
    while current_length < n:
        for i in range(0, n):
            j = i + current_length
            if j < n:
                if i == j:
                    table[i][j] = True
                elif i > j:
                    table[i][j] = False
                elif s[i] == s[j] and current_length== 1:
                    table[i][j] = True
                elif s[i] == s[j] and table[i + 1][j - 1]:
                    print(s[i::j])
                    table[i][j] = True
                else:
                    table[i][j] = False
                if table[i][j] and j - i >= max_sequence:
                    max_sequence = j - i
                    max_seq_i = i
                    max_seg_j = j
        current_length += 1

    print(table[max_seq_i][max_seg_j], max_seq_i, max_seg_j)
    print(s[max_seq_i:max_seg_j+1])
    for i in range(0, n):
        print(table[i])

    # check the substring of length 2


s = "aebcbda"
palindromicSubstring(s)
