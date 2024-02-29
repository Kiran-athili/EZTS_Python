#write a python program to take dictionary as input and print keys and values of the dictionary
n=int(input('enter the no.of items:'))
d={}
for i in range(n):
    key=input('key:')
    value=input('value:')
    d[key]=value
print(d)
