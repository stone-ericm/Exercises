LOWER_BOUND = 0
UPPER_BOUND = 0

while True:
	# testcase = 1234
	x = 1234
	y = 1234
	if id(x) == id(y):
		UPPER_BOUND = ++x
		break
	else:
		x -= 1
		y -= 1
		print (x)

while True:
	x = 1
	y = 1
	if id(x) != id(y):
		LOWER_BOUND = ++x
		break
	else:
		x = y = --x