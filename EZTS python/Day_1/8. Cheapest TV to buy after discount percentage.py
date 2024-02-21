'''chef is looking to buy a TV and has shortlisted two models. The first one costs A rupees, while the second one costs B rupees.since there is a huge sale coming up on Chefzon, Chef can get a flat discount of C rupees on the first TV, and a flat discount of D rupees on the second one.help Chef determine which of the two TVs would be cheaper to buy during the sale.'''
print("Enter the price of the first tv ")
print("Enter the discount percent of the first tv ")
a,b=map(float,input().split(" "))
dp=(a*(b/100)) #discount price
tp1=(a-dp) #total price
print("The final price is ",tp1)
print("Enter the price of the second tv ")
print("Enter the discount percent of the second tv ")
c,d=map(float,input().split(" "))
dp2=(c*(d/100)) #discount price
tp2=(c-dp2) #total price
if  tp1>tp2 :
    print("Please purchase second tv")
 
elif tp1<tp2 :
    print("Please purchase first tv")
    
else :
    print("Please purchase any tv")
