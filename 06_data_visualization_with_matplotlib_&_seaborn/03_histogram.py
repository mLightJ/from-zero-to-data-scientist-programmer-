import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Histogram => used for showing the distribution of a dataset

ages = [22, 25, 27, 30, 32, 35, 40, 45, 50, 55, 60]

plt.hist(ages, bins=5, color='grey', edgecolor='black') # x-axis => ages, y-axis => frequency
plt.title('Age Distribution') # title of the chart
plt.xlabel('Age') # label for x-axis
plt.ylabel('Frequency') # label for y-axis
plt.show()


#NB: The 'bins' parameter in the histogram function determines how the data is grouped into intervals. 
# In this example, we have set it to 5, which means the ages will be grouped into 5 intervals. 
# Adjusting the number of bins can help to better visualize the distribution of the data.

# Lesson Learned:
# 1. Histograms are useful for showing the distribution of a dataset.
# 2. We can customize the histogram by changing the number of bins, colors, and adding titles and labels.