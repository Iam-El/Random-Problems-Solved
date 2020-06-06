def minimumdeletions(s):
    currentLength = 0
    maxSequence = 1
    maxSequence_i = 1
    maxSequence_j = 1
    n = len(s)
    table = [[0 for i in range(n)] for j in range(n)]
    while currentLength < n:
        for i in range(len(s)):
            j = i + currentLength
            if j < n:
                if i == j:
                    table[i][j] = 1
                elif s[i] == s[j] and currentLength == 1:
                    table[i][j] = 2
                elif s[i] != s[j] and currentLength > 1:
                    table[i][j] = max(table[i][j - 1], table[i + 1][j])
                elif s[i] == s[j] and currentLength > 1:
                    table[i][j] = 2 + table[i + 1][j - 1]
                else:
                    table[i][j] = 1
                if table[i][j] > maxSequence:
                    maxSequence = table[i][j]
                    maxSequence_i = i
                    maxSequence_j = j
        currentLength = currentLength + 1
    return len(s) - maxSequence
    # for i in range(0, n):
    #     print(table[i])

    # check the substring of length 2


s = "aba"
print(minimumdeletions(s))
