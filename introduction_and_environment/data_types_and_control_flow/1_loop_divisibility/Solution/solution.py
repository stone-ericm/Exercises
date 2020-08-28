# Code your solution here
import random

x = random.randrange(0, 50)

data = []

for each in range(0, x, 5):
    if each == 0:
        pass
    else:
        data.append(each)
for each in range(0, x, 7):
    if each == 0:
        pass
    else:
        data.append(each)


print(data)
