
def hourglassSum(arr):
    l1=[]
    for i in range(4):
        for j in range(4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1] +arr[i+2][j+2]
            l1.append(sum)
    return max(l1)