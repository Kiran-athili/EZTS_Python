#write a python program to print sum of maximum and minimum elements in a matrix using tuple.
r,c=int(input("Enter the number of rows ")),int(input("Enter the number of columns "))
print("Enter the elements with a single space")
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=0,0
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print("The sum of the elements in matrix is ",max+min)
