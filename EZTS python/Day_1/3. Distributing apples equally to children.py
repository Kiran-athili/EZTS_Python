#python program to print remaining apples after distributing apples equally to children.
a=int(input("Enter the apples: "))
b=int(input("Enter the children: "))
c=a%b
if c==0:
    print("no apples left")
else:
    print(f"apples left is {c}")
