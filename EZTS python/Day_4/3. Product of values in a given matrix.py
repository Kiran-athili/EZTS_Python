#write the python program to print the product of values in a given matrix
r,c=int(input("Enter the number of rows: ")),int(input("Enter the number of columns: "))
print("Enter the elements with a single space: ")
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)
