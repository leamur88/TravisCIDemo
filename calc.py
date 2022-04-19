"""Calculator Class"""


class Calculator:
    """Calculator Class"""

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

    @classmethod
    def collect_num(cls, string):
        """Collect Number"""
        try:
            return int(input(f"Enter your {string} number:\n"))
        except ValueError as error:
            raise ValueError from error

    @classmethod
    def collect_operator(cls):
        """Collect Operator"""
        i = input("Enter desired operator number:\n")
        if i not in ["+", "-", "/", "*"]:
            raise ValueError
        return i

    @classmethod
    def add(cls, number1, number2):
        """Add two numbers"""
        print(f"{number1} + {number2} = {number1 + number2}")
        return number1 + number2

    @classmethod
    def subtract(cls, number1, number2):
        """Subtract two numbers"""
        print(f"{number1} - {number2} = {number1 - number2}")
        return number1 - number2

    @classmethod
    def divide(cls, number1, number2):
        """Divide two numbers"""
        print(f"{number1} / {number2} = {number1 / number2}")
        return number1 / number2

    @classmethod
    def multiply(cls, number1, number2):
        """Multiply two numbers"""
        print(f"{number1} * {number2} = {number1 * number2}")
        return number1 * number2


if __name__ == '__main__':
    C = Calculator()
    C.calc()
    