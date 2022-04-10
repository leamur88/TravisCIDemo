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
				self.add(n1,n2)
			elif (operator == "-"):
				self.subtract(n1,n2)
			elif (operator == "/"):
				self.divide(n1,n2)
			elif (operator == "*"):
				self.multiply(n1,n2)


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
		print(f"{n1} + {n2} = {n1 + n2}")
		return n1 + n2

	def subtract(self, n1, n2):
		print(f"{n1} - {n2} = {n1 - n2}")
		return n1 - n2

	def divide(self, n1, n2):
		print(f"{n1} / {n2} = {n1 / n2}")
		return n1 / n2

	def multiply(self, n1, n2):
		print(f"{n1} * {n2} = {n1 * n2}")
		return n1 * n2


if __name__ == '__main__':
	c = Calcluator()
	c.calc()