x=input('enter gender:')
y=int(input('Enter the no.of items:'))
d={}
for i in range(y):
    key=input('Merch:')
    value=int(input('Price:'))
    d[key]=value
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*y)/100)
if y=='male':
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print('items-prices : discount-prices')
for i in d:
    print(f'{i}-{d[i]}:{l[j]}')
    j+=1
else:
    print('*'*20)
print(f'total bill:{bill}')
