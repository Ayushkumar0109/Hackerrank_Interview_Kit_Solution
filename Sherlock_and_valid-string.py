from collections import Counter
def isValid(s):
    a=Counter(s)
    b=list(a.values())
    l=list(set(a.values()))
    if len(set(a.values()))==1:
        return ("YES")
    elif len(set(a.values()))==2 :
        if b.count(l[0])==len(b)-1 and (l[1]==l[0]+1 or l[1]==1):
            return ("YES")
        elif b.count(l[1])==len(b)-1 and (l[0]==l[1]+1 or l[0]==1):
            return ("YES")

        else:
            return ("NO")    
    else:
        return ("NO") 
    