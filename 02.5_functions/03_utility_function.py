#1 Even Checker
def is_even(number):
    # Check if a number is even
    if number % 2 == 0:
        return True # If the number is even, return True
    return False # If the number is not even, return False

#2 Average Calculator
def average(numbers):
    total = 0
    counts = 0
    for number in numbers: # Loop through each number in the list
        total += number
        counts += 1
    return total / counts # Return the average by dividing the total by the count of numbers

#3 Maximum Finder
def find_maximum(numbers):
    if not numbers: # Check if the list is empty
        return None # If the list is empty, return None
    max_number = numbers[0] # Initialize max_number to the first element of the list
    for number in numbers:
        if number > max_number:
            max_number = number 
    return max_number


the_list = []
print("How many numbers do you want to average?: ")
count = int(input())
for i in range(count):
    num = float(input(f"Enter number {i + 1}: "))
    the_list.append(num)

feedback = is_even(9)
print(feedback)

avg = average(the_list)
print(f"The average is: {avg}")

largest_value = find_maximum(the_list)
print(f"The maximum value is: {largest_value}")