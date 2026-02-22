'''
Create a program that:
    Asks the user for their name
    Asks for their age
    Calculates their birth year
    Displays a friendly message
'''
print("======== Birth Year Calculator =========")
name = input("What is your name? ")
age = int(input("How old are you? ")) 
current_year = int(input("What year is this? "))
birth_year = current_year - age
print(f"Hi {name}, you were born in {birth_year}")
print("=====================================")