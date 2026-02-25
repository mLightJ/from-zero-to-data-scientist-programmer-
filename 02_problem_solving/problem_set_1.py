# ===================================
# Even or Odd Checker
#Ask the user for a number and print: "Even number" if it's even, and "Odd number" if it's odd.
# ===================================

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:    print("Odd number")

# ===================================
# Prblem 2 - Calculator
# Ask the user for: first number, second number and Operation (+, -, *, /). Perform the operation and print the result.
# ===================================
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose an operation (+ - * /): ")

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        result = "Error: Division by zero"
    else:
        result = first_number / second_number
else:
    result = "Invalid operation"

print(f"Result: {first_number} {operation} {second_number} = {result}")

# ===================================
# Problem 3 - Largest of Three Numbers
# Ask the user for three numbers and print the largest one.
# ===================================
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")