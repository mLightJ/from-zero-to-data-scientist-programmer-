import numpy as np
from scipy import stats
import pandas as pd

ages = [5, 7, 8, 5, 6, 9, 10, 5, 7, 8]

# Calculate mean, median, and standard deviation

mean = np.mean(ages) # The mean is calculated by summing all the values and dividing by the number of values.
print("Mean:", mean)
median = np.median(ages) # The median is the middle value when the data is sorted. If there is an even number of values, it is the average of the two middle values.
print("Median:", median)
std_dev = np.std(ages) # The standard deviation measures the amount of variation or dispersion in a set of values. A low standard deviation indicates that the values tend to be close to the mean, while a high standard deviation indicates that the values are spread out over a wider range.
print("Standard Deviation:", std_dev)
variance = np.var(ages) # The variance is the average of the squared differences from the mean. It is a measure of how much the values in a dataset vary.
print("Variance:", variance)

range_value = max(ages) - min(ages) # The range is the difference between the maximum and minimum values in the dataset. It gives an idea of the spread of the data.
print("Range:", range_value)

# Calculate mode // Note: mode returns the value(s) that appear most frequently in the data. 
# If there are multiple modes, it will return all of them.

mode = stats.mode(ages) 
print("Mode:", mode.mode)


df = pd.DataFrame({'ages': ages})
print(df.describe())


#ND: Why use median instead of mean in analyzing salary data?
# The median is often preferred over the mean when analyzing salary data because 
# salary distributions are typically skewed, with a small number of high earners significantly 
# increasing the mean. The median provides a better representation of the typical salary by 
# indicating the middle value, which is less affected by outliers and extreme values. 
# This allows for a more accurate understanding of the central tendency of the salary data.