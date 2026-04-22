import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

'''
salary = [3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 50000]
ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

mean_salary = np.mean(salary)
print("Mean Salary:", mean_salary)

median_salary = np.median(salary)
print("Median Salary:", median_salary)


range_value = max(ages) - min(ages) # The range is the difference between the maximum and minimum values in the dataset. 
# It gives an idea of the spread of the data.
print("Range of Ages:", range_value)


variance_salary = np.var(salary) # The variance is the average of the squared differences from the mean. 
# It is a measure of how much the values in a dataset vary.
print("Variance of Salary:", variance_salary)

std_dev_salary = np.std(salary) # The standard deviation is the square root of the variance. It is a measure of the average distance of each value from the mean.
print("Standard Deviation of Salary:", std_dev_salary)'''

scores = [10, 25, 45, 60, 80, 90, 95]

print("CENTER")
print(f"Mean:   {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")

print("\nSPREAD")
print(f"Std Dev: {np.std(scores):.2f}")
print(f"IQR:     {np.percentile(scores,75) - np.percentile(scores,25):.2f}")
print(f"Range:   {max(scores) - min(scores)}")