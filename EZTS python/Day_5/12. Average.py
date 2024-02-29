d={}
for i in range(n):
    k=input('enter rollno.:')
    v={}
    for j in range(m):
        sub=input('enter subject name:')
        marks=int(input('enter marks:'))
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f'{i}:{sum(l)/m}')
