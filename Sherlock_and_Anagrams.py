
def sherlockAndAnagrams(s):
    l1=[]
    sum=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sum+=l1.count(sorted(s[i:j]))
            l1.append(sorted(s[i:j]))
    return sum  