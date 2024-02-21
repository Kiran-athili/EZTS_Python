#python program to check a number is strong or not.
def strongNum(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        return "strong number"
    else:
        return "Not s strong number"
n=int(input())
print(strong(n))
