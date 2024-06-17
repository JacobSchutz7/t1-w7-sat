# class definition
class Dog:
	# definition of class attributes
	def __init__(self, name, breed, colour):
		self.name = name
		self.breed = breed
		self.colour = colour
	# definition of class methods
	def bark(self):
		return f"{self.name} says Woof!"

# create an object of the Dog class by calling the constructor and assigning it to a variable
my_dog = Dog("Jerry", "Kelpie", "brown")
# call the bark() class method
print(my_dog.bark())