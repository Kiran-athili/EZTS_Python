#write a python program to print prime numbers in a range using functions.
def primeinrange(n,m):
    for i in range(n,m+1):
        a=0
        for j in range(1,i+1):
            if i%j==0:
                a+=1
        if a==2:
            print(i)
n,m=int(input()),int(input())
primeinrange(n,m)
    
