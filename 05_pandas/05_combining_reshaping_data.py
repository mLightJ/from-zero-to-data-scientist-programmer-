import pandas as pd

# Concatenating DataFrames
'''
df1 = pd.DataFrame({
    "name": ["Joel", "Ama"],
    "age": [22, 21]
})

df2 = pd.DataFrame({
    "name": ["Kwame", "Abena"],
    "age": [23, 20]
})

df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)'''

# Merging DataFrames based on a common column

students = pd.DataFrame({
    "name": ["Joel", "Ama", "Kwame"],
    "program_id": [1, 2, 1]
})

programs = pd.DataFrame({
    "program_id": [1, 2],
    "program_name": ["ICT", "Business"]
})

df_merged = pd.merge(students, programs, on="program_id")
print(df_merged)


# Types of merges: inner, left, right, outer

df_inner = pd.merge(students, programs, on="program_id", how="inner")  # Inner join
df_left = pd.merge(students, programs, on="program_id", how="left")  # Left join
df_right = pd.merge(students, programs, on="program_id", how="right")  # Right join
df_outer = pd.merge(students, programs, on="program_id", how="outer")  # Outer join



# Lessson Learned:
# - Concatenating DataFrames using pd.concat()
# - Merging DataFrames using pd.merge()
# - Types of merges: inner, left, right, outer