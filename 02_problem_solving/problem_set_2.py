#====================================================
#Ask the user for a number N: Calculate the sum of all numbers from 1 to N and print the result.
'''
    Use a loop (for preferred)
    Do NOT use the built-in sum() function
    Store result in a variable
    Print clean output
'''


'''number = int(input("Enter a number N: "))
total_sum = sum(range(1, number + 1))
print(f"The sum of all numbers from 1 to {number} is: {total_sum}")
'''
'''
number = int(input("Enter a number N: "))
total_sum = 0
for num in range(1, number + 1):
    total_sum += num
print(f"The sum of all numbers from 1 to {number} is: {total_sum}")
'''
#====================================================

#====================================================
#Multiplication Table Generator
'''Ask the user for a number, Print it's multiplication table from 1 - 10
multiplication_table_number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{multiplication_table_number} x {i} = {multiplication_table_number * i}")

'''
#====================================================

#====================================================
#
'''Create a simple password system:
    Set a password inside the code (e.g., "python123")
    User has 3 attempts
    If correct → print "Access Granted"
    If wrong 3 times → print "Access Denied"
    
'''
password = "python123"
user_attempts = 3


for attempt in range(1, user_attempts + 1):
    print("=========================3 ATTEMPT PASSWORD SYSTEM===========================")
    
    print(f"Attempt {attempt} of {user_attempts}")
    
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access Granted")
        break
        
    else:
        if attempt == user_attempts:
            print("Attempt limit reached. Access Denied.")
    
print("Program ended.")
#====================================================
