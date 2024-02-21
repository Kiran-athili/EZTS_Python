#write a python program to find given number is prime number or not?
n=int(input("Enter a number: "))
for i in range(2,int(n**0.5)+1):
    if n%i==0:
       print("It is a prime number")
else:
    print("Not a prime number")
       
    
