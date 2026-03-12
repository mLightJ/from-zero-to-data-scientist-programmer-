#DICTIONARY FOR STORING STUDENT RECORDS
student_records = {
    'name': 'John Doe', 
    'age': 20, 
    'course': 'Computer Science', 
    'grade': 'A'
}

print("Student Name:", student_records['name']) # Accessing the name
student_records['grade'] = 'B' # Updating the grade
student_records['email'] = 'john.doe@example.com' # Adding a new field

print("Updated Student Records:", student_records)

# Explaination:
# A dictionary is a collection of key-value pairs.
'''
    key     → value
    name    → John Doe
    age     → 20
    course  → Computer Science
    Grade   → A
'''