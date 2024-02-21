#Each pizza consists of 4 slices.There are N friends and each friend needs exactly X slices.
#Find the number of pizzas they should order to satisfy their appetite.
print("Each pizza contains 4 slices")
N=int(input("Enter the no of friends: "))
X=int(input("Enter the no of slices needed for each friend: "))
TS=N*X
if TS%4==0 :
    TP=TS//4
else :
    TP=(TS//4)+1
print("No of pizzas needed is: ",TP)
    

