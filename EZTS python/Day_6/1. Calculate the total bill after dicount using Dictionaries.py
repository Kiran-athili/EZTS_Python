#a shopping mall gives a discount to men 5% and 7% dicount for women and individual discount on each item is 3%*no.of items.calculate the total bill using Dictionaries. 
d={}
n=int(input("Enter the number of items"))
for i in range(n):
    k=input("Enter item: ")
    v=int(input("Enter the value of the products"))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]*(3*n)/100)
g=input("Enter gender: ")
if g=="male":
    bill=sum(1)-sum(1)*5/100
else:
    bill=sum(1)-sum(1)*7/100
j=0
print("items-prices : discount-prices")
for i in d :
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"Total bill : {bill}")
