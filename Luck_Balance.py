def luckBalance(k, contests):
    sum=0
    l=[]
    for val in contests:
        sum+=val[0]
        if val[1]==1:
            l.append(val[0])
    for i in range(len(l)-k):
        sum=sum-(2*min(l))
        l.remove(min(l))
    return sum    