'''Chef is looking to buy a TV and has shortlisted two models. The first one costs A rupees, while the second one costs B rupees.
Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of C rupees on the first TV, and a flat discount of D rupees on the second one.
Help Chef determine which of the two TVs would be cheaper to buy during the sale.
Input Format
• The first line contains a single integer T - the number of test cases. Then the test cases follow.
• The first and only line of each test case contains four space-separated integers A, B, C and D - '''
A=int(input("enter the cost of first TV: "))
B=int(input("enter the cost of second TV: "))
C=int(input("enter the discount amount of first TV: "))
D=int(input("enter the discount amount of second TV: "))
if A-C < B-D:
    print("first TV is cheaper to buy")
elif A-C > B-D:
    print("second TV is cheaper to buy")
else :
    print("Any")
    
