from calculation import Calculations

class Calculator:
    def __init__(self):
        self.ops = Calculations()

    def main(self):
        while True:
            # take input from the user
            selection = input("Please select operation -\n"
                              "1. Addition\n"
                              "2. Subtract\n"
                              "3. Multiply\n"
                              "4. Divide\n"
                              "5. Floor\n"
                              "6. Exponent\n"
                              "7. Modulus\n")

            # Confirm the arithmetic function selected
            if selection in ('1', '2', '3', '4', '5', '6', '7'):
                try:
                    num1 = int(input("Please enter the first number: "))
                    num2 = int(input("Please enter the second number: "))

                # Error handling in case a number wasn't entered
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                # Arithmetic functions based on selected method
                if selection == '1':
                    print(num1, "+", num2, "=", self.ops.addition(num1, num2))

                elif selection == '2':
                    print(num1, "-", num2, "=", self.ops.subtraction(num1, num2))

                elif selection == '3':
                    print(num1, "*", num2, "=", self.ops.multiply(num1, num2))

                elif selection == '4':
                    try:
                        print(num1, "/", num2, "=", self.ops.division(num1, num2))
                    except ValueError as e:
                        print(e)

                elif selection == '5':
                    print(num1, "//", num2, "=", self.ops.floor(num1, num2))

                elif selection == '6':
                    print(num1, "**", num2, "=", self.ops.exponent(num1, num2))

                elif selection == '7':
                    print(num1, "%", num2, "=", self.ops.modulus(num1, num2))

                # Continue calculating check
                # break the loop if the answer is no
                continue_calculating = input("Are more calculations required? (y/n): ")
                if continue_calculating.lower() == "n":
                    break

if __name__ == "__main__":
    calc = Calculator()
    calc.main()