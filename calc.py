"""Calculator Class"""


class Calculator:
    """Calculator Class"""

    def __init__(self):
        return

    def calc(self):
        """Calculator Constructor"""
        while 1:
            print("What basic operation would you like to do")
            number1 = self.collect_num("first")
            operator = self.collect_operator()
            number2 = self.collect_num("second")
            if operator == "+":
                self.add(number1, number2)
            elif operator == "-":
                self.subtract(number1, number2)
            elif operator == "/":
                self.divide(number1, number2)
            elif operator == "*":
                self.multiply(number1, number2)

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
    c = Calculator()
    c.calc()
