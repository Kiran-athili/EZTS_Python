#write a python program to print sum of the given matrix
r,c=int(input("Enter the no of Rows: ")),int(input("Enter the no of columns: "))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
