n=int(input('Enter the no.of contacts:'))
d={}
for i in range(n):
    key=input('Name:')
    value=input('Contact:')
    d[key]=value
print(d)
while n>0:
    a=input('Enter the contact you want to search:')
    if a in d:
        print(d[a])
    else:
        print('Not found')
