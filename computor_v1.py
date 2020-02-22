
errors = {"validation" : "Validation error. You have to use allowed characters"}

def computor():
	print("Hello, I can resolve a polynom!")
	str_ = input("Enter your polynom->")
	if not is_string_valid:
		print(errors["validation"])
		return









def is_string_valid(str_):
	allowed_char = ['x', 'X', '^', '-', '=', ' ', '	', '*']
	# and numbers
	for c in str_:
		if not(allowed_char.has(c) || c.isdigit()):
			return False
	return True



if __name__ == "__main__":
	computor()
	pass