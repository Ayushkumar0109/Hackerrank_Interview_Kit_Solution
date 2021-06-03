from itertools import combinations
def minimumAbsoluteDifference(arr):
    a=sorted(arr)
    min=abs(a[0]-a[1])
    for i in range(1,len(a)-1):
        if abs(a[i]-a[i+1]) < min:
            min=abs(a[i]-a[i+1])
    return min   