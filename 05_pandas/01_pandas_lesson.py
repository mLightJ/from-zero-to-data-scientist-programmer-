import pandas as pd     # Import the pandas library

# Create a dictionary with sample data manually, which will be used to create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 
    'Age': [25, 30, 35, 40, 45],
    'Course': ['Computer Science', 'Mathematics', 'Physics', 'Computer Science', 'Mathematics']
}

df = pd.DataFrame(data)
print(df)