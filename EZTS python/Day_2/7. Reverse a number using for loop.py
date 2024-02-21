#reverse a number using for loop.
n=int(input("Enter a number: "))
rev=0
for i in range(n):
    if a>=0:
        b=a%10
        rev=rev*10+b
        a//=10
    else:
        break
print(rev)
