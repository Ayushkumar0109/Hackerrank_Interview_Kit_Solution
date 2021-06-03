from collections import Counter
def whatFlavors(cost, money):
    d=Counter(cost)
    for sunny in cost:
        johnny=money-sunny
        if sunny!=johnny:
            if d[johnny]>0:
                j=cost.index(johnny)
                print(cost.index(sunny)+1,j+1)
                break
        else:
            if d[johnny]>1:
                j=cost[cost.index(johnny)+1:].index(johnny)
                print(cost.index(sunny)+1,j+2+cost.index(sunny))
                break
        
            