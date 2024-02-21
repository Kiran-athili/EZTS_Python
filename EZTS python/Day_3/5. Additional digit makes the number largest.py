'''You have a positive number of length n and one additional digit.
You can insert this digit anywhere in the number, including at the beginning or at the end.
Your task is to make the result as large as possible.
For example, you have the number 76543, and the additional digit is 4. Then the maximum number you can get is 765443, and it can be obtained in two ways — by inserting a digit after the 3th the 4th digit of the number.'''
s,d=map(str,input().split())
for i in range(len(s)):
    if int(s[i]) <= int(d):
        print(s[:i]+d+s[i:])
        break
else:
    print(s+d)

