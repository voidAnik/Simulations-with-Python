def reverse(s):
    return s[::-1]

string=str(input('Give a string= '))
r_str=reverse(string)

if(string==r_str):
    print("This is a palindrome")
else:
    print("This is not a palindrome")