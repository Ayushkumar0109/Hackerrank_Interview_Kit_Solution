def countInversions(arr):
    count=0
    while arr!=sorted(arr):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
                count+=1
    return count    
a=[int(x) for x in input().split()]
b=countInversions(a)
print(b)    