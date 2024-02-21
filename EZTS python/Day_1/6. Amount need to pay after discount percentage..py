#Alice buys a toy with a selling price of 100 rupees. There is a discount of z percent on the toy. Find the amount Alice needs to pay for it.
a=int(input("selling price of toy is: "))
z=int(input("Enter the discount percentage: "))
b=a-(a*z/100)
print("amount need to pay is: ",b)
