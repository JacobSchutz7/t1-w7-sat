def personal_details(**kwargs):
	for key, value in kwargs.items():
		print(f"{key} ---> {value}")

personal_details(name="Jacob", age="27", city="Adelaide")

def myfunction(*onestar, **twostars):
	print("args:", onestar)
	print("kwargs:", twostars)

myfunction("meme", "meme", "meme", one="lmao", two="lmao", three="lmao")