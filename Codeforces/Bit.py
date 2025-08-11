n=int(input())
l=[]
v=0
for i in range(n):
    s=input()
    if '+' in s:
        v+=1
    elif '-' in s:
        v-=1
print(v)