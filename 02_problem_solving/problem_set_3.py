'''
1 Prime Number Checker
2 Number Guessing Game
3 List Analyzer (manual version without built-ins)
4 Pattern Printing
5 Dictionary Analyzer
6 Frequency Counting
7 Word Frequency Counter
'''

#1 Prime Number Checker
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
         print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#2 Number Guessing Game
guess_number = 4
guess_count = 0

while guess_count < 3:
    print("You have", 3 - guess_count, "guesses left.")
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == guess_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < guess_number:
        print("Too low! Try again.")
    else:        print("Too high! Try again.")
else:
    print("Sorry, you didn't guess the number.")
    
    
#3 List Analyzer (manual version without built-ins)
numbers = []
total = 0

user_range = int(input("How many numbers do you want to enter? "))
for i in range(user_range):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]  # Initialize largest to the first element
smallest = numbers[0]  # Initialize smallest to the first element

for num in numbers:
    if num > largest:
        largest = num
        
    if num < smallest:
        smallest = num
        
    total += num

average = total / len(numbers)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
print(f"The total is: {total}")
print(f"The average is: {average}")


#4 Pattern Printing
numbers = [12,5,8,20,3,15,7]
even_numbers = []
numbers_greater_than_10 = []
every_number_is_squared = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        
    if num > 10:
        numbers_greater_than_10.append(num)
        
    every_number_is_squared.append(num ** 2)
    
print("Even numbers:", even_numbers)
print("Numbers greater than 10:", numbers_greater_than_10)
print("Every number squared:", every_number_is_squared)


#5 Dictionary Analyzer
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Dave": 95,
    "Eve": 88
}

highest_grade = max(student_grades.values())
lowest_grade = min(student_grades.values())

print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)



#6 Frequency Counting (e.g., 4 appears 4 times, 3 appears 3 times, etc.)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num, count in frequency.items():
    print(f"{num} appears {count} times")
        
#7 Word Frequency Counter
text = input("Enter a sentence: ")
word_frequency = {}

for word in text.split():
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, count in word_frequency.items():
    print(f"'{word}' appears {count} times")
    
    
'''    
Mini Project — Text Analyzer
Create a program that asks the user for a sentence and outputs:

1 Total words
2 Unique words
3 Most common word
4 Frequency of every word
'''

sentence = input("Enter a sentence: ")
words = sentence.split()
total_words = len(words)
unique_words = len(set(words))
most_common_word = max(set(words), key=words.count)
word_frequency = {word: words.count(word) for word in set(words)}

print(f"Total words: {total_words}")    
print(f"Unique words: {unique_words}")
print(f"Most common word: {most_common_word}")
print("Word frequency:")

for word, count in word_frequency.items():
    print(f"'{word}': {count}")
    
    

# List Comprehensions, Counter and Lambda Functions

from collections import Counter

num = [3,8,15,2,9,12,7,6]
data = [1,2,2,3,3,3,4,4,4,4]
dec = [10,4,7,2,15]

no_greater_than_7 = [x for x in num if x > 7] # List comprehension to filter numbers greater than 7
squared_numbers = [x ** 2 for x in num] # List comprehension to square each number in the list
count = Counter(data) # Using Counter to count the frequency of each element in the data list

dec.sort(key=lambda x: x, reverse=True) # Sort in descending order

print(no_greater_than_7)
print(squared_numbers)
print(count)
print(dec)