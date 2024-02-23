#Write a python program to print average of the given matrix elements
r,c=int(input("Enter the number of rows ")),int(input("Enter the number of columns "))
print("Enter the elements with a single space")
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
avg=0
for i in l:
    print(i)
    avg+=sum(i)/(r*c)
print("The average of the elements in matrix is ",avg)
