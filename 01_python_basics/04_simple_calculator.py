'''
Create a mini calculator program that:
Asks the user to enter two numbers
Asks the user to choose an operation:
    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)

Performs the chosen operation
Displays the result in a clear format
'''

print("========== SIMPLE CALCULATOR ==========")
# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get user input for operation
print("Choose an operation:")
print("Addition (+)")
print("Subtraction (-)")
print("Multiplication (*)")
print("Division (/)")
operation = input("Choose an operation: ")

# Perform the chosen operation
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result:.3f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")