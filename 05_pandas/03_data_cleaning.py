import pandas as pd

'''
df = pd.read_csv('04_python_for_data/dirty_students.csv')  # Read the CSV file into a DataFrame
print(df)  # Print the first few rows of the DataFrame to check for missing values and data types


# Check for missing values in the DataFrame

print(df.isnull())  # Print a DataFrame of the same shape as df with True for missing values and False for non-missing values
print(df.isnull().sum())  # Print the count of missing values in each column of the DataFrame

# Handling missing values

# Option 1: Drop rows with at least one missing values
df = df.dropna()  # Drop rows with at least one missing value

df.dropna(inplace=True)  # Drop rows with at least one missing value and modify the original DataFrame in place
print(df)  # Print the DataFrame after dropping rows with missing values

# Option 2: Fill missing values with a specific value (e.g., 0 for numeric columns, 'Unknown' for categorical columns)

df["age"].fillna(0, inplace=True)  # Fill missing values in the 'age' column with 0 and modify the original DataFrame in place
print(df)  # Print the DataFrame after filling missing values in the 'age' column

df["course"].fillna("Unknown", inplace=True)  # Fill missing values in the 'course' column with 'Unknown' and modify the original DataFrame in place
print(df)  # Print the DataFrame after filling missing values in the 'course' column

df["grade"].fillna(df["grade"].mean(), inplace=True)  # Fill missing values in the 'grade' column with the mean of the column and modify the original DataFrame in place
print(df)  # Print the DataFrame after filling missing values in the 'grade' column


# Option 3: Removing duplicates rows from the DataFrame

print(df.duplicated().sum())  # Print the count of duplicate rows in the DataFrame
df.drop_duplicates(inplace=True)  # Drop duplicate rows and modify the original DataFrame in place
print(df)  # Print the DataFrame after dropping duplicate rows


# Option 4: Renaming columns in the DataFrame

df.rename(columns={"name": "student_name", "age": "student_age", "course": "student_course", "grade": "student_grade"}, inplace=True)  # Rename columns and modify the original DataFrame in place
print(df)  # Print the DataFrame after renaming columns


# Option 5: Fixing data types of columns in the DataFrame

print(df.dtypes)  # Print the data types of each column in the DataFrame
df["student_age"] = df["student_age"].astype(int)  # Convert the 'student_age' column to integer data type
'''


# Lesson Learned:
# - Identifying missing values in a DataFrame
# - Handling missing values in a DataFrame
# - Removing duplicate rows from a DataFrame
# - Renaming columns in a DataFrame
# - Fixing data types of columns in a DataFrame