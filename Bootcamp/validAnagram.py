def isAnagram(s, t):
    length1 = len(s)
    length2 = len(t)
    dict1 = {}
    dict2 = {}
    isTrue = False
    if length1 != length2:
        return False
    elif s == "" and t == "":
        return True
    else:
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] = dict1[s[i]] + 1
        for i in range(len(t)):
            if t[i] not in dict2:
                dict2[t[i]] = 1
            else:
                dict2[t[i]] = dict2[t[i]] + 1
        for j in dict1:
            if j not in dict2:
                return False
            elif dict1[j] != dict2[j]:
                return False
        return True

a=isAnagram("hello","hellos")
print(a)