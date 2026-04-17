import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# scatter plot => used for showing the relationship between two variables

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [50, 55, 60, 65, 70, 75, 80, 85]

plt.scatter(study_hours, exam_scores, color='black') # x-axis => study_hours, y-axis => exam_scores
plt.title('Study Hours vs. Exam Scores') # title of the chart
plt.xlabel('Study Hours') # label for x-axis
plt.ylabel('Exam Scores') # label for y-axis
plt.show()

#NB: The scatter plot is a powerful tool for visualizing the relationship between two variables. 
# In this example, we can see that there is a positive correlation between study hours and exam scores, 
# meaning that as study hours increase, exam scores also tend to increase.

# Lesson Learned:
# 1. Scatter plots are useful for showing the relationship between two variables.
# 2. We can customize the scatter plot by changing the colors, adding titles and labels.