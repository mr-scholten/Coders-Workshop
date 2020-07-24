

def isAnagram(str1, str2):
    str1Arr = sorted(str1)
    str2Arr = sorted(str2)
    print(str1Arr)
    print(str2Arr)
    sort1 = "".join(str1Arr)
    sort2 = "".join(str2Arr)
    if sort1 == sort2:
        return True
    else:
        return False
    return True

print(isAnagram("map", "pam"))