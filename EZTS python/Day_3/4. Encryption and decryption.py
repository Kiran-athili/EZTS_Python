#write a python program to make encryption and decryption with a key value using functions.
def encryption(s,k):
    s1=""
    for i in s:
        x=ord(i)+k
        s1+=chr(x)
    print(s1)
def decryption(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)
    print(s1)
k=int(input("Enter key values: "))
s=input("Enter the string: ")
op=input("Select operation: ")
if op=="encrypt":
    encryption(s,k)
elif op=="decrypt":
    decryption(s,k)
else:
    print("Improper operation")
