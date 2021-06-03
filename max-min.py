def maxMin(k, arr):
    a=sorted(arr)
    l=[]
    for i in range(len(arr)+1-k):
        l.append(a[i+k-1]-a[i])
    return min(l)    
