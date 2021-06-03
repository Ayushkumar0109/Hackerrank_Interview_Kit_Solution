
#
from itertools import combinations
def commonChild(s1, s2):
    l3=list(s1)
    l4=list(s2)
    l1=list(s1)
    l2=list(s2)
    for val in l3:
        if val not in l2:
            l1.remove(val)
    if len(l1)==0:
        return 0        
    for val in l4:
        if val not in l1:
            l2.remove(val)
    if len(l1)==1 or len(l2)==1:
        return 1 
    l=''
    s=''               
    if len(l1)<=len(l2):
        l=l.join(l1)
        s=s.join(l2)
    else:
        l=l.join(l2)
        s=s.join(l1)
    i=len(l) 
    print(i)       
    while i>=1:
        for val in combinations(l,i):
            s1=(''.join(val))
            if s.find(s1)!=-1:
                return i
        i=i-1        
a=commonChild("HARRY","SALLY")
print(a)                      