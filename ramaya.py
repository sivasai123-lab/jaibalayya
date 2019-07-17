from itertools import combinations
s,p=map(int,input().split())
m=len(str(s))
a=list(combinations(str(s),m-p))
a.sort()
print(*a[0],sep='')
