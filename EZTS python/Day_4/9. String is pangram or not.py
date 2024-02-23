#write a python program to check given string is panagram or not
import string
s=input ()
s=s.lower()
s1=string.ascii_lowercase
if set(s) == set(sl):
    print("Panagram")
else:
    print("Not a panagram")
