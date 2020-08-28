# Code your solution here
string = input("Please input an all uppercase or all lowercase phrase\n")

if string.isupper():
    string = string.lower()
    print(string)
elif string.islower():
    string = string.upper()
    print(string)
else:
    print("Input error")
