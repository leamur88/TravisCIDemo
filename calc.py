

def calc():
	while 1:
		print("What basic operation would you like to do")
		n1 = collectNum("first")
		operator = collectOperator()
		n2 = collectNum("second")
		if (operator == "+"):
			add(n1,n2)
		elif (operator == "-"):
			subtract(n1,n2)
		elif (operator == "/"):
			divide(n1,n2)
		elif (operator == "*"):
			multiply(n1,n2)


def collectNum(s):
	try:
		return int(input(f"Enter your {s} number:\n"))
	except ValueError:
		raise ValueError

def collectOperator():
	i = input(f"Enter desired operator number:\n")
	if i not in ["+", "-", "/", "*"]:
		raise ValueError
	return i

def add(n1, n2):
	print(f"{n1} + {n2} = {n1 + n2}")
	return n1 + n2

def subtract(n1, n2):
	print(f"{n1} - {n2} = {n1 - n2}")
	return n1 + n2

def divide(n1, n2):
	print(f"{n1} / {n2} = {n1 / n2}")
	return n1 / n2

def multiply(n1, n2):
	print(f"{n1} * {n2} = {n1 * n2}")
	return n1 * n2


if __name__ == '__main__':
	calc()