LOWER_BOUND = 0
# UPPER_BOUND = 0

###Number needs to be positive

def upper_binary_search(testcase):
	x = testcase+1
	y = testcase+1
	if id(x) != id(y):
		x//=2
		y//=2
		# print(y)
		if id(x) == id(y):
			while id(x) == id(y):
				x+=1
				y+=1
				# print(y)
			# UPPER_BOUND = x
			# print(UPPER_BOUND)
			return(x-1)
		else:
			return(upper_binary_search(x))
			# return()
	else:
		return("Int is too low")

def lower_search(testcase):
	x = testcase+1
	y = testcase+1
	if id(x) == id(y):
		while id(x) == id(y):
			x-=1
			y-=1
		return(x+1)
	else:
		return("Int is too high")

UPPER_BOUND = upper_binary_search(1233)
LOWER_BOUND = lower_search(0)
# print(UPPER_BOUND)
# print(LOWER_BOUND)