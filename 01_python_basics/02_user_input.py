'''
Create a program that:

    Asks the user for:
    Their name
    Their age
    Their favorite programming language
    Then displays a profile summary.
'''
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
fav_programming_language = input("Please enter your favorite programming language: ")

print("========== PERSONAL PROFILE ==========")
print(f"Name: {name}")   
print(f"Age: {age} years old")
print(f"Favorite Programming Language: {fav_programming_language}")