
errors = {"validation" : "Validation error. You have to use allowed characters"}



collect_of_pol = [
"1 * X^0 + 2 * X^2 + 3 * X^2 + 1 * X^1 -12 * x^1 = 12 * X ^2", 
"1 * X^0 + 2 * X^2 + 3 * X^2 + 1 * X^1 -12 * x^1 = 0 * x^0",
'9.1 * x ^ 1 = 2 * x ^ 2',
"42 * x^0 = 15 * x^2 "
]



def is_string_valid(str_):
	allowed_char = ['x', 'X', '^', '-', '=', ' ', '	', '*', '+', '.']
	for c in str_:
		if c not in allowed_char and c.isdigit() == False:
			print(c)
			return False
	return True

def parser(str_):
	enum = {'number_scan':1, 'pow_scan':2, 'transitional' : 3}
	state = enum['number_scan']
	stack = {"1" : [], '2' : [], '0' : []}
	sign = 1.0

	num = ""
	for id, item in enumerate(str_):
		print("cycle", item, state, stack, num)
		if state == enum['number_scan']:
			if item == ' ' or item == '	':
				continue
			if item.isdigit() or item == '-' or item == '+' or item == '.':
				num+=str(item)
			if item == '*':
				state = enum['transitional']
		elif (item == ' ' or item == '	') and state == enum['transitional']:
			print("go to ttrans",item, state)
			state = enum['pow_scan']
		elif item == 'X' or item == 'x' or item == '^' and state == enum['pow_scan']:
			continue
		elif item.isdigit() and state == enum['pow_scan']:
			print("place",item)
			stack[str(item)].append(float(num) * sign)
			num = ""
			state = enum['number_scan']
		else:
			print("else?")
		if item == '=':
			print("find  = ")
			sign = -1.0
		# if item == 'X' or item == 'x'
	return(stack)



def computor():
	print("Hello, I can resolve a polynom!")
	str_ = input("Enter your polynom->")
	if not is_string_valid(str_):
		print(errors["validation"])
		return
	print("Sucssess")
	stack = parser(str_)
	print(stack)

if __name__ == "__main__":
	computor()
	pass