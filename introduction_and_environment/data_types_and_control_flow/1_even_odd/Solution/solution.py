# Code your solution here
number = int(input())
if number % 2 == 0:
    data = "Even"
elif number % 2 != 0:
    data = "Odd"
else:
    data = "error"

print(data)
