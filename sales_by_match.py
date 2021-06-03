def sockMerchant(n, ar):
    l1=[]
    sum=0
    for i in range(n):
        if ar[i] not in l1:
            s=ar.count(ar[i])
            sum+=(s//2)
            l1.append(ar[i])
    return sum        
            