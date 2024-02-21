#write a python program to print sum of odd composite numbers in a given range
def composite(n):
    c=0
    for i in range (l,n+l):
        if n%==0:
            c+=1
        if c>2:
            return l
        else:
            return 0
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    if i%2!=0:
        flag=composite(i)
        if flag==l:
            l.append(i)
print(sum(l))
print(l)
    
           
