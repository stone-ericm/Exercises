LOWER_BOUND = 0
UPPER_BOUND = 0

x = 1
y = 1

while True:
	# testcase = 1234

	if id(x) != id(y):
		UPPER_BOUND = x-1
		break
	else:
		x += 1
		y += 1

x = 1
y = 1

while True:
	if id(x) != id(y):
		LOWER_BOUND = x+1
		break
	else:
		x -= 1
		y -= 1
