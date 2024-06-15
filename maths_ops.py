# Using *args
def add(*args):
	sum = 0
	for each in args:
		sum += each
	return sum

def subtract(*args):
	diff = 0
	for each in args:
		diff -= each
	return diff

def multiply(*args):
	product = 1
	for each in args:
		product *= each
	return product

print(multiply(3, 1, 20))