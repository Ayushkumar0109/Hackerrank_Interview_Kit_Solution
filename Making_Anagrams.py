
from collections import Counter
def makeAnagram(a, b):
    a1=Counter(a)
    b1=Counter(b)
    sum=0
    for val in a1:
        if val in b1.keys():
            sum+=abs(a1[val]-b1[val])
        else:
            sum+=a1[val]
    for val in b1:
        if val not in a1.keys():
            sum+=b1[val]
    return sum 