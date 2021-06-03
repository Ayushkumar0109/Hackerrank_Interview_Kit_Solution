from collections import Counter
def freqQuery(queries):
    l=[]
    a=Counter()
    for val in queries:
        if val[0]==1:
            if val[1] in a.keys():
                a[val[1]]+=1
            else:
                a[val[1]]=1
        elif val[0]==2:
            if val[1] in a.keys() and a[val[1]]>0:
                a[val[1]]-=1
        else:
            l.append(1 if val[1] in set(a.values()) else 0)
    return l