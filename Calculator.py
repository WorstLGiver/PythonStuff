# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function modulus two numbers
def modulus(x, y):
    return x % y


# This function powers two numbers
def exponent(x, y):
    return x ** y


# This function floor divides two numbers
def floor_divide(x, y):
    return x // y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Modulus")
print("7.Floor Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # Check if choice is one of the seven options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", exponent(num1, num2))

        elif choice == '6':
            print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '7':
            print(num1, "//", num2, "=", floor_divide(num1, num2))

        break
    else:
        print("Invalid Input")
