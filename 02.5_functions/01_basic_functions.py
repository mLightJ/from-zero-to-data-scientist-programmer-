'''
    def
    parameters
    return values
    reusable logic
    modular programming

#1 Greet user

import numbers


def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user("Bob")

#2 Add two numbers

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)

#3 Analyze numbers
def analyze_numbers(a, b):
    total = a + b
    difference = a - b
    product = a * b
    return total, difference, product

result = analyze_numbers(3, 5)
print(f"Sum: {result[0]}")
print(f"Difference: {result[1]}")
print(f"Product: {result[2]}")
'''

#4 list analyzer
'''
    The function should take a list of numbers and return:
    largest number
    smallest number
    sum
    average
    
    using loops and conditionals
'''
list_to_analyze = [1, 2, 3, 4, 5] # example list to analyze

def analyze_list(numbers):
    largest = numbers[0] # initialize largest and smallest to the first element of the list
    smallest = numbers[0]
    total = 0
    
    # loop through the list to find the largest, smallest, and total
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total += num
    
    average = total / len(numbers)
    return largest, smallest, total, average # return a tuple containing the results

largest, smallest, total, average = analyze_list(list_to_analyze) # unpacking the returned tuple into separate variables
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Total: {total}")
print(f"Average: {average}")

