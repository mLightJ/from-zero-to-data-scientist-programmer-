# List of 3 student dictionaries
students = [
    {"name": "Alice", "age": 20, "course": "Computer Science", "grade": "A"},
    {"name": "Bob", "age": 21, "course": "Mathematics", "grade": "B"},
    {"name": "Charlie", "age": 19, "course": "Physics", "grade": "C"}
]

for student in students:
    print(f"Name: {student['name']} | Course: {student['course']} | Grade: {student['grade']}")
    

# Lesson learned:
# - A list can contain dictionaries, which allows us to store complex data structures.
# - We can iterate through the list of dictionaries to access and display specific information about each student
# - List => rows, Dictionary => columns
# - Data frame => rows and columns (like a table)