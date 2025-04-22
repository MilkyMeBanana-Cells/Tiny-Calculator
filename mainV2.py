# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Define lists for each operation
add_ops = ["add", "Add", "ADD", "+"]
sub_ops = ["subtract", "Subtract", "SUBTRACT", "-"]
mul_ops = ["multiply", "Multiply", "MULTIPLY", "*"]
div_ops = ["divide", "Divide", "DIVIDE", "/"]

while True:  # Loop until a valid operation is entered
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("That's not a number! Please try again.\n")
        continue

    operation = input("What operation would you like to do? Type add, subtract, multiply, or divide. ").strip()

    # Perform the chosen operation
    if operation in add_ops:
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
        break
    elif operation in sub_ops:
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
        break
    elif operation in mul_ops:
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)
        break
    elif operation in div_ops:
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)
        break
    else:
        print("Not a valid operation. Please try again.\n")
