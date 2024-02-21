'''Timur loves codeforces. That's why he has a string s having length 10 made containing only ercase Latin letters. Timur wants to know how many Indices strings differs from the string "code.ces".
For example string = "coolforses" differs from "codeforces" In 4 Indices, shown in bold.
Help Timur by finding the number of indices where string differs from "codeforces".
Note that you can't reorder the characters in the strings.'''
s=input("Enter  a string: ")
s1="codeforces"
count=0
for i in range(len(s1)):
    if s1[i]!=s[i]:
        count+=1
print(count)
