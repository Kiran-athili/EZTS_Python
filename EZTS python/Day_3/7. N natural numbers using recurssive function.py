#Write a python program to print n natural numbers using recursion function.
print("Enter the number")
def printing(n):
    if n<1:
        return 1
    else:
        printing(n-1)
        print(n)
n=int(input())
printing(n)
