def countingValleys(steps, path):
    count=0
    a=0
    sum=0
    for i in range(steps):
        a=sum
        if path[i]=='U':
            sum+=1
        else:
            sum-=1
        if sum==0 and a==-1:
            count+=1
    return count          