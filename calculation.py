

class Calculations:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

    def floor(self, num1, num2):
        return num1 // num2

    def exponent(self, num1, num2):
        return num1 ** num2

    def modulus(self, num1, num2):
        return num1 % num2