def rotLeft(a, d):
    l1=[0]*len(a)
    for i in range(len(a)):
        if i-d>=0:
            l1[i-d]=a[i]
        else:
            l1[len(a)-d+i]=a[i]
    return l1 