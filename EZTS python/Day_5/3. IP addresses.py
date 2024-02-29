d={}
n,m=map(int,input().split())
for i in range(n):
    k,v=map(int,input().split())
    d[k]=v
for i in range(n):
    k1,v1=map(str,input().split())
    for i in d:
        if d[i]==value1[:-1]:
            print(f'(k1) (v1) #(i)')
