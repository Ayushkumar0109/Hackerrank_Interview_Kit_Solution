
def arrayManipulation(n, queries):
    l=[0]*(n+1)
    for a,b,c in queries:
        l[a-1]+=c
        l[b]-=c
    max=0
    sum=0
    for val in l:
        sum+=val
        if sum > max:
            max=sum
    return max