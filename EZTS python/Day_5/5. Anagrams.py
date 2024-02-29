a=input()
b=input()
if len(a)==len(b):
    if sorted(a)==sorted(b):
        print('True')
    else:
        print('False')
else:
    print('False')
