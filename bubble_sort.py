def countSwaps(a):
    count=0
    for i in range(len(a)):
        if a== sorted(a):
            break
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                count+=1
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    print("Array is sorted in",count, end=" ")
    print("swaps.")
    print("First Element:", a[0])
    print("Last Element:",a[len(a)-1])           
