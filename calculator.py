def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def divide(a,b):
	if b == 0:
		"Error! Cannot divide by 0!"
		return
	return a / b

def multiply(a,b):
	return a * b

def get_user_input():
	operation = input("Enter operation ( + - * /): ")
	if operation not in ['+', '-', '*', '/']:
		print("Invalid operation")
		return 
	
	a = float(input("Enter first number: "))
	b = float(input("Enter second number: "))

	return operation, a, b

def main():
	while True:
		operation, num1, num2 = get_user_input()
		result = 0
		if operation == '+':
			result = add(num1, num2)
		elif operation == 'i':
			result = subtract(num1, num2)
		elif operation == '*':
			result = multiply(num1, num2)
		else:
			result = divide(num1, num2)

		print(f"The result is: {result}")

		input("Would you like to do another calculation?: ")

main()