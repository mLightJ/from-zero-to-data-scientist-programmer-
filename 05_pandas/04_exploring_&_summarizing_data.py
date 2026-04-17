import pandas as pd

df = pd.read_csv('04_python_for_data/students.csv')
#print(df.describe()) # Print summary statistics for the DataFrame

#print(df["age"].value_counts()) # Print the count of each unique value in the 'grade' column

#print(df["course"].unique()) # Print the unique values in the 'grade' column
#print(df["course"].nunique()) # Print the number of unique values in the 'grade' column

#df.sort_values("age", ascending=True, inplace=True) # Sort the DataFrame by the 'age' column
#df.sort_values("age", ascending=False, inplace=True) # Sort the DataFrame by the 'grade' column
#print(df)

'''
print(df.groupby("course")["age"].mean())
print(df.groupby("course")["age"].min())
print(df.groupby("course")["age"].max())
print(df.groupby("course")["age"].std())
print(df.groupby("course")["age"].count())
'''

df["birth_year"] = 2026 - df["age"]
print(df["birth_year"].dtypes)


# Lesson Learned:
# - Using .describe() to get summary statistics for a DataFrame
# - Using .value_counts() to get the count of each unique value in a column
# - Using .unique() and .nunique() to get the unique values and number of unique values in a column
# - Using .sort_values() to sort a DataFrame by a column
# - Using .groupby() to group data by a column and perform operations on the grouped data