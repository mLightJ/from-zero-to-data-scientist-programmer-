'''
Create a program that:
Asks the user to enter:
    First number
    Second number
Converts them to float
Calculates and displays:
    Sum
    Difference
    Product
'''
# Get user input & Convert to float
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))


# Calculate sum, difference, and product
sum_result = first_number + second_number
difference_result = first_number - second_number
product_result = first_number * second_number

# Display results
print("========== CALCULATION RESULTS ==========")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")