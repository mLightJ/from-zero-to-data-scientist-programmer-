import pandas as pd

df = pd.read_csv('04_python_for_data/students.csv')  # Read the CSV file into a DataFrame
#print(df)  # Print the DataFrame to the console
#print(df.iloc[0, 0])
#print(df.iloc[2:4])
#print(df.loc[df['name'] == 'Ursula'])  # Print the value in the 'name' column for the row where the index is 6 using .loc
#print(df.iloc[7])
#print(df[['name', 'age']].head())  # Print the first few rows of the 'name' and 'age' columns of the DataFrame
print(df[df['course'] == 'Data Science'])  # Print rows where the 'course' column is 'Data Science'

# Accessing data
'''
print(df.head())  # Print the first few rows of the DataFrame
print(df.tail())  # Print the last few rows of the DataFrame 
print(df.info())  # Print information about the DataFrame, including data types and non-null counts
print(df.describe())  # Print summary statistics for the DataFrame, including count, mean, std, min, 25%, 50%, 75%, and max for numeric columns
print(df.columns)  # Print the column names of the DataFrame
print(df.index)  # Print the index of the DataFrame (row labels)
print(df.dtypes)  # Print the data types of each column in the DataFrame
print(df['name'])  # Print the 'Name' column of the DataFrame  
print(df['age'])  # Print the 'Age' column of the DataFrame
print(df['course'])  # Print the 'Course' column of the DataFrame
print(df['name'][0])  # Print the first value in the 'Name' column
print(df['age'][0])  # Print the first value in the 'Age' column
print(df['course'][0])  # Print the first value in the 'Course' column


# Accessing rows and columns

print(df.loc[0])  # Print the first row of the DataFrame using .loc
print(df.loc[1])  # Print the second row of the DataFrame using .loc
print(df.loc[df['name'] == 'Alice'])  # Print rows where the 'Name' column is 'Alice' using .loc
print(df.loc[df['age'] > 30])  # Print rows where the 'Age' column is greater than 30 using .loc
print(df.loc[df['course'] == 'Mathematics'])  # Print rows where the 'Course' column is 'Mathematics' using .loc

# Accessing rows and columns using iloc

print(df.iloc[0])  # Print the first row of the DataFrame using .iloc
print(df.iloc[1])  # Print the second row of the DataFrame using .iloc
print(df.iloc[0, 0])  # Print the value in the first row and first column of the DataFrame using .iloc
print(df.iloc[0, 1])  # Print the value in the first row and second column of the DataFrame using .iloc

print(df.iloc[0:3])  # Print the first three rows of the DataFrame using .iloc
print(df.iloc[0:3, 0:2])  # Print the first three rows and first two columns of the DataFrame using .iloc

# Filtering data and selecting specific columns and rows

print(df[['name', 'course']])  # Print only the 'Name' and 'Course' columns of the DataFrame
print(df[df['age'] > 30])  # Print rows where the 'Age' column is greater than 30  
print(df[df['course'] == 'Mathematics'])  # Print rows where the 'Course' column is 'Mathematics'
print(df[df['grade'] == 'A'])  # Print rows where the 'Grade' column is 'A'

# Accessing specific values using .at

print(df.at[0, 'name'])  # Print the value at the first row and 'Name' column using .at
print(df.at[0, 'age'])  # Print the value at the first row and 'Age' column using .at
print(df.at[0, 'course'])  # Print the value at the first row and 'Course' column using .at
'''



# Lesson Learning points:
# 1. Reading CSV files into a DataFrame using pd.read_csv()
# 2. Accessing data in a DataFrame using various methods such as .loc, .iloc, and .at
# 3. Filtering data in a DataFrame based on conditions
# 4. Selecting specific columns and rows in a DataFrame