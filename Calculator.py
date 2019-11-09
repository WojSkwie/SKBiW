import sys


class Calculator:

    def __init__(self, value1, value2, char):
        self.value1 = value1
        self.value2 = value2
        self.char = char

    @staticmethod
    def add(value1, value2):
        return value1+value2

    @staticmethod
    def subtract(value1, value2):
        return value1 - value2

    @staticmethod
    def multiply(value1, value2):
        return value1 * value2

    @staticmethod
    def divide(value1, value2):
        if value2 == 0:
            return "You can't divide by 0. >:("
        else:
            return value1/value2

    def calculate(self):
        math_operation = {"+": self.add, "-": self.subtract, "*": self.multiply, "/": self.divide}
        if self.char not in math_operation:
            print("Sorry, char must be one of these: + - * /")
        else:
            print(math_operation[self.char](self.value1, self.value2))
