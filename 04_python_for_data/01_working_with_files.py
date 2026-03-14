# Working with files
# Open a file for reading
#file = open('data.txt', 'r')

# Read the contents of the file
#contents = file.read()

# Close the file
#file.close()

# Open a file for writing
#file = open('output.txt', 'w')

# Write some text to the file
#file.write('Hello, world!')

#======================================================================
# ex1 CSV file reading 4.1
'''
Write a Python script to:
    Open the file
    Read each line
    Split each line by commas
    Store the data as a list of dictionaries
'''

students = []
with open("04_python_for_data/students.csv", "r") as file: # Open the file for reading
    next(file)  # Skip the first line (header)
    for line in file:
        name, age, course, grade = line.strip().split(",") # Split the line by commas and unpack the values
        students.append({"name": name, "age": int(age), "course": course, "grade": float(grade)})

print(students)
#======================================================================

#======================================================================
#ex2 CSV file writing 4.1.1
'''
Write a Python script to:
    Create a list of dictionaries representing students
    Open a new CSV file for writing
    Write the header row
    Write each student's data as a new line in the CSV file
'''
students = [
    {"name": "Melly", "age": 20, "course": "Math", "grade": 85.5},
    {"name": "Ermona", "age": 22, "course": "Science", "grade": 90.0},
    {"name": "Korro", "age": 21, "course": "History", "grade": 78.0}
]

with open("04_python_for_data/students_write.csv", "w") as file: # Open the file for writing
    file.write("Name,Age,Course,Grade\n")  # Write the header row
    for student in students:
        line = f"{student['name']},{student['age']},{student['course']},{student['grade']}\n" # Create a line for each student
        file.write(line)  # Write the line to the file
        
student_write = []
with open("04_python_for_data/students_write.csv", "r") as file: # Open the file for reading
    next(file)  # Skip the first line (header)
    for line in file:
        name, age, course, grade = line.strip().split(",") # Split the line by commas and unpack the values
        student_write.append({"name": name, "age": int(age), "course": course, "grade": float(grade)})

print(student_write)
#======================================================================

#======================================================================
#ex3 CSV file reading and writing 4.1.2
'''
Write a Python script to:
    Read the students.csv file
    Calculate the average grade for each course
    Write the results to a new CSV file called course_averages.csv with two columns: Course and Average Grade
'''
course_grades = {}
with open("04_python_for_data/students.csv", "r") as file: # Open the file for reading
    next(file)  # Skip the first line (header)
    for line in file:
        name, age, course, grade = line.strip().split(",") # Split the line by commas and unpack the values
        grade = float(grade) # Convert the grade to a float
        if course not in course_grades: # If the course is not already in the dictionary, add it with an empty list
            course_grades[course] = [] # Create a list to store the grades for the course
        course_grades[course].append(grade)

#print(course_grades)

with open("04_python_for_data/course_averages.csv", "w") as file: # Open the file for writing
    file.write("Course,Average Grade\n")  # Write the header row
    for course, grades in course_grades.items():
        average = sum(grades) / len(grades) # Calculate the average grade for the course
        line = f"{course},{average}\n" # Create a line for the course and average grade
        file.write(line)  # Write the line to the file

with open("04_python_for_data/course_averages.csv", "r") as file: # Open the file for reading
    next(file)  # Skip the first line (header)
    for line in file:
        course, average = line.strip().split(",") # Split the line by commas and unpack the values
        print(f"Course: {course}, Average Grade: {average}")
#======================================================================

# Lesson learned in this exercise:
# - Working with files in Python
# - Reading and writing data in CSV files
