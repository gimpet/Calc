
#Arithemic function of addition
def Addition(num1,num2):
    return num1 + num2

#Arithemtic function of subsctraction
def Subtraction(num1, num2):
    return num1 - num2

#Arithmetic function of multiplication
def Multiply(num1, num2):
    return num1 * num2

#Arithmetic function of division
def Division( num1, num2):
    return num1 / num2

#Arithmetic function of Flooring
def Floor( num1, num2):
    return num1 // num2

#Arithmetic function of Exponential calculations
def Exponent( num1, num2):
    return num1 ** num2

#Arithmetic function of Modulus
def Modulus( num1, num2):
    return num1 % num2

while True:

    # take input from the user
    Selection = input("Please select operation -\n" \
        "1. Addition\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Floor\n" \
        "6. Exponent\n" \
        "7. Modulus\n")
    
    # Confirm the arithmetic function selected
    if Selection in ('1', '2', '3', '4','5','6','7'):
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
     
         #Error handling in case a number wasn't entered       
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        #Arithmetic functions based on selected method       
        if Selection == '1':
            print(num1, "+", num2, "=", Addition(num1, num2))

        elif Selection == '2':
            print(num1, "-", num2, "=", Subtraction(num1, num2))

        elif Selection == '3':
            print(num1, "*", num2, "=", Multiply(num1, num2))

        elif Selection == '4':
            print(num1, "/", num2, "=", Division(num1, num2))

        elif Selection == '5':
            print(num1, "//", num2, "=", Floor(num1, num2))

        elif Selection == '6':
            print(num1, "**", num2, "=", Exponent(num1, num2))

        elif Selection == '7':
            print(num1, "%", num2, "=", Modulus(num1, num2))    

        
        # Continue calculating check
        # break the loop if the answer is no
        continue_calculating = input("Are more calculations required? (y/n): ")
        if continue_calculating == "n":
          break