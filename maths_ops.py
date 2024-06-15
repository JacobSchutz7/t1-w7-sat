# Using *args
def add(*args):
	sum = 0
	for each in args:
		sum += each
	return sum

def subtract(*args):
	diff = args[0]
	for each in args[1:]:
		diff -= each
	return diff

def multiply(*args):
	product = 1
	for each in args:
		product *= each
	return product