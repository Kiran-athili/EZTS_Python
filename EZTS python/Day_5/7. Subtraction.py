a=list(map(int,input().split()))
print(a)
b=int(input('enter the value to be subtracted:'))
for i in range(len(a)):
    for j in range(len(a)):
        if a[j]-a[i]==b:
            print('true')
            break
          
