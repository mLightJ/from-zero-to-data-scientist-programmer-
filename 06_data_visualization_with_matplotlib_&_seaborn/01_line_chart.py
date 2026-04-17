import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Line chart => used for showing trends over time

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 150, 200, 250, 300, 350]

plt.plot(months, sales, marker='o', color='red') # x-axis => months, y-axis => sales 
plt.title('Monthly Sales') # title of the chart
plt.xlabel('Month') # label for x-axis
plt.ylabel('Sales') # label for y-axis
plt.show()

#NB: The 'marker' parameter in the plot function adds markers to the data points on the line chart. 
# In this example, we have set it to 'o', which means that each data point will be marked with a circle. 
# You can choose different marker styles such as 's' for square, '^' for triangle, and 'D' for diamond.


# Lesson Learned:
# 1. Line charts are useful for showing trends over time.
# 2. We can customize the line chart by adding markers, changing colors, and adding
#    titles and labels.