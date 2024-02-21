#The amount can be withdrawn must be multiple of 5
a=float(input("Enter the withdraw amount: "))
b=float(input("Balance amount: "))
if b>a:
    if a%5==0:
        print("amount can be withdrawn")
        c=b-a
        print("Balance amount: ",c)
        
    else :
        print("amount is not multiple by 5")
else:
    print("Insufficient amount")
