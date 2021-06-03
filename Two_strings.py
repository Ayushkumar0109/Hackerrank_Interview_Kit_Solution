def twoStrings(s1, s2):
    for val in s1.strip():
        if val in s2.strip():
            return "YES"
    return "NO"    