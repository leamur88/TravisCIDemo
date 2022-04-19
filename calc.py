class Calculator:
	def __init__(self):
		return

	def calc(self):
		while 1:
			print("What basic operation would you like to do")
			n1 = self.collectNum("first")
			operator = self.collectOperator()
			n2 = self.collectNum("second")
			if (operator == "+"):
				result = self.add(n1,n2)
			elif operator == "-":
				result = self.subtract(n1,n2)
			elif operator == "/":
				result = self.divide(n1,n2)
			elif operator == "*":
				result = self.multiply(n1,n2)
			else:
				raise ValueError
			print(f"{n1} {operator} {n2} = {result}")

	def collectNum(self, s):
		try:
			return int(input(f"Enter your {s} number:\n"))
		except ValueError:
			raise ValueError

	def collectOperator(self):
		i = input(f"Enter desired operator number:\n")
		if i not in ["+", "-", "/", "*"]:
			raise ValueError
		return i

	def add(self, n1, n2):
		return n1 + n2

	def subtract(self, n1, n2):
		return n1 - n2

	def divide(self, n1, n2):
		return n1 / n2

	def multiply(self, n1, n2):
		return n1 * n2


if __name__ == '__main__':
	c = Calculator()
	c.calc()