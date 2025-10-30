#pallindrom.py
palindrom=str(input(" Enter your value of palindrom="))

lenth =len(palindrom)


if palindrom[:lenth//2:] == palindrom[-1:lenth//2:1]:
    print("yess its an palindrome   ")
else:
    print("its niot an palindrome ")


