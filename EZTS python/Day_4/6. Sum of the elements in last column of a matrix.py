#Write a python program to print the sum of the elements in last column of a matrix
r,c=int(input("Enter the number of rows ")),int(input("Enter the number of columns "))
print("Enter the elements with a single space")
l,sum=[],0
for i in range(r):
    l.append(list(map(int,input().split())))
for i in l:
    sum+=i[c-1]
print(sum)
