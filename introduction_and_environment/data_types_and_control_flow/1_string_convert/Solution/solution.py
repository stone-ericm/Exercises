# Code your solution here
string = input()

if string.isupper():
    string = string.lower()
    print(string)
elif string.islower():
    string = string.upper()
    print(string)
else:
    print("Input error")
