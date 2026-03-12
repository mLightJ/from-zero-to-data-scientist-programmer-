students = [
    {"name": "Alice", "age": 20, "course": "Computer Science", "grade": "A"},
    {"name": "Bob", "age": 21, "course": "Mathematics", "grade": "B"},
    {"name": "Charlie", "age": 19, "course": "Physics", "grade": "C"},
    {"name": "David", "age": 22, "course": "Computer Science", "grade": "B"},
    {"name": "Eve", "age": 21, "course": "Mathematics", "grade": "A"},
    {"name": "Frank", "age": 20, "course": "Physics", "grade": "C"},
    {"name": "Grace", "age": 19, "course": "Computer Science", "grade": "B"},
    {"name": "Henry", "age": 22, "course": "Mathematics", "grade": "A"},
    {"name": "Ivy", "age": 21, "course": "Physics", "grade": "C"},
]

highest_grade = students[0]["grade"] # Initialize the highest and lowest grades with the first student's grade
lowest_grade = students[0]["grade"]  # We will compare the grades of the remaining students with these initial values to find the actual highest and lowest grades in the list.
top_students = [students[0]["name"]]
bottom_students = [students[0]["name"]]

cs_students = 0
math_students = 0
physics_students = 0

for student in students [1:]: # Start iterating from the second student since we have already initialized the highest and lowest grades with the first student's grade
    if student["grade"] < highest_grade: # Compare the current student's grade with the highest grade found so far
        highest_grade = student["grade"]
        top_students = [student["name"]] # If the current student's grade is higher than the highest grade, update the highest grade and reset the list of top students to include only this student
        
    elif student["grade"] == highest_grade: # If the current student's grade is equal to the highest grade, add this student to the list of top students
        top_students.append(student["name"])
        
    if student["grade"] > lowest_grade:
        lowest_grade = student["grade"]
        bottom_students = [student["name"]]
    
    elif student["grade"] == lowest_grade:
        bottom_students.append(student["name"])
        
    if student["course"] == "Computer Science":
        cs_students += 1
    if student["course"] == "Mathematics":
        math_students += 1
    if student["course"] == "Physics":
        physics_students += 1
        
print(f"Highest Grade: {highest_grade} | Top Students: {top_students}")
print(f"Lowest Grade: {lowest_grade} | Bottom Students: {bottom_students}")
print(f"Number of Computer Science Students: {cs_students}")
print(f"Number of Mathematics Students: {math_students}")
print(f"Number of Physics Students: {physics_students}")


# Lesson learned:
# - Manual dataset analysis without built-in functions
# - lists, dictionaries, loops, counters, comparisons, tie-handling logic
# - what is tie-handling logic? When multiple students have the same highest or lowest grade, we need to handle this situation by keeping track of all students who share that grade. 
        # This is done by maintaining a list of top students and bottom students, and updating these lists accordingly when we find a new highest or lowest grade.