class Calculator:
    def __init__(self):
        return

    def calc(self):
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

    def collect_num(self, string):
        try:
            return int(input(f"Enter your {string} number:\n"))
        except ValueError:
            raise ValueError

    def collect_operator(self):
        i = input("Enter desired operator number:\n")
        if i not in ["+", "-", "/", "*"]:
            raise ValueError
        return i

    def add(self, number1, number2):
        print(f"{number1} + {number2} = {number1 + number2}")
        return number1 + number2

    def subtract(self, number1, number2):
        print(f"{number1} - {number2} = {number1 - number2}")
        return number1 - number2

    def divide(self, number1, number2):
        print(f"{number1} / {number2} = {number1 / number2}")
        return number1 / number2

    def multiply(self, number1, number2):
        print(f"{number1} * {number2} = {number1 * number2}")
        return number1 * number2


if __name__ == '__main__':
    c = Calculator()
    c.calc()
