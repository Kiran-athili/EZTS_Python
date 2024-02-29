l,d=map(int,input().split())
a=list(map(int,input().split()))
flag=0
for i in a:
    for j in a:
        if i=j==d:
            flag=1
x=True if flag==1 else false
print(x)
