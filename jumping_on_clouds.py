def jumpingOnClouds(c):
    count=0
    i=0
    while i<len(c):
        if i==len(c)-1:
            break
        if i==len(c)-2:
            count+=1
            break
        if c[i+2]==0:
            i+=2
        else:
            i+=1
        count+=1
    return count            