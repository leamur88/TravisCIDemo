"""Calculator Class"""

# pylint: disable=no-member


class Calculator:
    """Calculator Class"""

    def __init__(self):
        return

    def calc(self):
        """Calculator Constructor"""
        while 1:
            print("What basic operation would you like to do")
            num_1 = self.collectNum("first")
            operator = self.collectOperator()
            num_2 = self.collectNum("second")
            if operator == "+":
                result = self.add(num_1, num_2)
            elif operator == "-":
                result = self.subtract(num_1, num_2)
            elif operator == "/":
                result = self.divide(num_1, num_2)
            elif operator == "*":
                result = self.multiply(num_1, num_2)
            else:
                raise ValueError
            print(f"{num_1} {operator} {num_2} = {result}")

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
        return number1 + number2

    @classmethod
    def subtract(cls, number1, number2):
        """Subtract two numbers"""
        return number1 - number2

    @classmethod
    def divide(cls, number1, number2):
        """Divide two numbers"""
        return number1 / number2

    @classmethod
    def multiply(cls, number1, number2):
        """Multiply two numbers"""
        return number1 * number2


if __name__ == '__main__':
    C = Calculator()
    C.calc()
    