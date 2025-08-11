n,k=map(int,input().split())
a=list(map(int,input().split()))
t=a[k-1]
c=0
for i in a:
    if i>0 and i>=t:
        c+=1
    if i<t:
        break
print(c)