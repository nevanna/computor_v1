
errors = {"validation" : "Validation error. You have to use allowed characters"}


# Examples:
#  5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
#  4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
#  5 * X^0 + 4 * X^1 = 4 * X^0
#  1 * X^0 + 4 * X^1 = 0
#  8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0
#  5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
#  5 + 4 * X + X^2= X^2
#



collect_of_pol = [
"1 * X^0 + 2 * X^2 + 3 * X^2 + 1 * X^1 -12 * x^1 = 12 * X ^2", 
"1 * X^0 + 2 * X^2 + 3 * X^2 + 1 * X^1 -12 * x^1 = 0 * x^0",
'9.1 * x ^ 1 = 2 * x ^ 2',
"42 * x^0 = 15 * x^2 ",
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
"5 * X^0 + 4 * X^1 = 4 * X^0",
"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
"4 * X^0 + 1 * X^2 = 1 * X^2",
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
			state = enum['pow_scan']
		elif item == 'X' or item == 'x' or item == '^' and state == enum['pow_scan']:
			continue
		elif item.isdigit() and state == enum['pow_scan']:
			stack[str(item)].append(float(num) * sign)
			num = ""
			state = enum['number_scan']
		else:
			print("else?")
		if item == '=':
			sign = -1.0
	return(stack)

def get_pol_degree(stack):
	_max = 0
	for deg in stack:
		if _max < int(deg) and len(stack[deg]) > 0:
			_max = int(deg)
	return _max


def computor():
	print("Hello, I can resolve a polynom!")
	str_ = input("Enter your polynom->")
	if len(str_) == 0 or not is_string_valid(str_):
		print(errors["validation"])
		return
	print("Sucssess")
	stack = parser(str_)
	print(stack)
	# to norm form 

	
	print("deg->", get_pol_degree(stack))

if __name__ == "__main__":
	computor()
	pass