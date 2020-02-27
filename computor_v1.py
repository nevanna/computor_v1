
errors = {"validation" : "Validation error. You have to use allowed characters",
"max_pow": "Wrong max_pow"}
# http://edu.glavsprav.ru/info/diskriminant/

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
"4 * X^0 + 1 * X^2 = 1 * X^3",
"4 * X^0 + 2 * X^1 = 0", 
"- 4 * X^0 - 2 * X^2 = 0"
]

def ft_abs(n):
	if n < 0:
		return n*(-1)
	else:
		return n

def ft_sqrt(n):
	eps = float(1e-15)
	x = 1.0
	while True:
		nx = float(x + n / x) / 2;
		if ft_abs(x - nx) < eps:
			break
		x = nx
	print(x)
	return x


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
	# stack = {"1" : [], '2' : [], '0' : []}
	stack = {"1" : 0, '2' : 0, '0' : 0}
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
			# stack[str(item)].append(float(num) * sign)
			if str(item) not in stack.keys():
				exit("Error degree more than 2")
			stack[str(item)]+=float(num) * sign
			num = ""
			state = enum['number_scan']
		else:
			print("else?")
		if item == '=':
			sign = -1.0
	return(stack)

def try_convert_to_int(nb):
	int_nb = int(nb)
	if nb - float(int_nb) == 0:
		return int_nb
	return nb
	

def get_max_pow(stack):
	_max = 0
	for deg in stack:
		if _max < int(deg) and stack[deg] != 0 and stack[deg] != 0.0:
			_max = int(deg)
	return _max

def solve_full_quadratic_equation(a, b, c):
	D = b*b - 4*a*c
	print("D =", D)
	if D > 0:
		x_1 = (-b - ft_sqrt(D)) / (2 * a)
		x_2 = (-b + ft_sqrt(D)) / (2 * a)
		x_1 = try_convert_to_int(x_1)
		x_2 = try_convert_to_int(x_2)
		print("The solution is", x_1,"and", x_2)
	elif D == 0:
		x = (-b) / (2 * a)
		x = try_convert_to_int(x)
		print("The solution is", x)
	elif D < 0:
		re = (-1) * b / ( 2 * a)
		re = try_convert_to_int(re)
		im = (ft_abs(D) / (4 * a * a))
		im = try_convert_to_int(ft_sqrt(try_convert_to_int(im)))
		x_1 = ((str(re) + " + ") if re != 0.0 else "") + str(im) + "i"
		x_2 = (str(re) if re != 0.0 else "") + " - " + str(im) + "i"
		print("The solution is", x_1, "and", x_2)

def solve_quadratic_equation(stack):
	a = stack['2']
	b = stack['1']
	c = stack['0']
	if a == 0:
		exit("I can't solve it")
	solve_full_quadratic_equation(a, b, c)

def solve_equation(stack):
	a = stack['1']
	b = stack['0']
	if a == 0.0 and b == 0.0:
		print("The solutions are all numbers")
		return
	x = b * (-1) / a
	x = try_convert_to_int(x)
	print("The solution is", x)
	
def standart_form(stack, max_pow):
	f_x = ""

	for el in range(max_pow, -1, -1):
		el = str(el)
		t = try_convert_to_int(stack[el])
		if t == 0.0:
			continue
		t = ("+ " + str(t)) if t >= 0 else ("- " + str(abs(t)))
		
		if el == '0':
			 f_x += str(t) + " "
		elif el == '1':
			f_x += str(t) + "X "
		elif el == '2':
			f_x += str(t) + "X^" + el + " "
	f_x += "= 0"
	if f_x[0] == "+":
		f_x = f_x[2::]
	print("Reduced form:", f_x)


def computor():
	print("Hello, I can resolve a polynom!")
	str_ = input("Enter your polynom->")
	if len(str_) == 0 or not is_string_valid(str_):
		print(errors["validation"])
		return
	stack = parser(str_)
	print(stack)
	# to norm form 
	max_pow = get_max_pow(stack)
	print("Polynomial degree:", max_pow)
	standart_form(stack, max_pow)

	if max_pow == 2:
		solve_quadratic_equation(stack)
	elif max_pow == 1:
		solve_equation(stack)
	# elif max_pow == 0:
	# else:
	# 	print(errors["max_pow"])
	# 	return 


if __name__ == "__main__":
	computor()
	pass