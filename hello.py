n=int(input())
s=[]
q=[]
o=[]
u=[]
c=0
for i in range(0,n):
    h=input()
    s.append(h)
for i in s:
    for j in range(0,len(i)+1):
        q.append(i[:j])
for i in q:
    if i!='':
        u.append(i)
for i in u:
    o.append(q.count(i))
for i in range(0,len(o)):
    c=c+1
    if o[i]!=n:
        break
print(u[c-2])
