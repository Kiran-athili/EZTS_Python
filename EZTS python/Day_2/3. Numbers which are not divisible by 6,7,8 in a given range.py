#write a python program to print the numbers which are not divisible by 6,7,8 in a given range.
a=int(input("enter a number: "))
b=int(input("enter last number: "))
for i in range(a,b+1):
    if i%6!=0 and i%7!=0 and i%8!=0 :
       print(i)
