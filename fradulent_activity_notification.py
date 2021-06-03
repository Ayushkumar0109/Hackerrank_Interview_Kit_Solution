import statistics
def activityNotifications(expenditure, d):
    count=0
    l=[]
    s=[]
    for i in range(len(expenditure)-d):
        l.append(2*(statistics.median(expenditure[i:i+d])))
        s.append(expenditure[i+d])
    print(l)
    print(s)    
    for i in range(len(l)):
        if s[i]>=l[i]:
            count+=1
    return count
n=int(input())
size=int(input())
a=[int(x) for x in input().split()]
res=activityNotifications(a,size)
print(res)                
