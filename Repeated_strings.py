def repeatedString(s, n):
    s1=n//len(s)
    sum=s1*s.count('a')
    s2=n%len(s)
    s3=s[:s2]
    sum+=s3.count('a')
    return sum