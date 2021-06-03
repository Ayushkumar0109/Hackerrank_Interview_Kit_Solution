def maximumToys(prices, k):
    sum=0
    c=0
    while sum<=k:
        sum+=min(prices)
        if sum<=k:
            c+=1
        prices.remove(min(prices))
    return c    
