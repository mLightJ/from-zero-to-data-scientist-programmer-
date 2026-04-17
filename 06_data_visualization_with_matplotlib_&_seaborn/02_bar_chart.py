import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Bar chart => used for comparing categories

programs = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
students = [50, 40, 30, 20, 10]

plt.bar(programs, students, color='blue') # x-axis => programs, y-axis => students
plt.title('Number of Students in Programming Courses') # title of the chart
plt.xlabel('Programming Language') # label for x-axis
plt.ylabel('Number of Students') # label for y-axis
plt.show()


#NB: The 'color' parameter in the bar function allows you to specify the color of the bars in the chart. 
# In this example, we have set it to 'blue', which means all the bars will be colored blue. 
# You can choose different colors for the bars by using color names (e.g., 'red', 'green', 'orange') or hexadecimal color codes (e.g., '#FF5733').

# Lesson Learned:
# 1. Bar charts are useful for comparing categories.
# 2. We can customize the bar chart by changing the colors, adding titles and labels.