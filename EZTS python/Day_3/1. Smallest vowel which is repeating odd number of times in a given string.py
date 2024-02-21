#write a python program to print the smallest vowel which is repeating odd number of times in a given string.
s=input("Enter a string: ")
s1=""
for i in s:
    if i in "aeiouAEIOU":
       if s.count(i)%2!=0:
            s1+=i
print(min(s1))
