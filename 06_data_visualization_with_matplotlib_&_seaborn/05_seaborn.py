import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "programming_language": ["Python", "JavaScript", "Java", "C++", "Ruby"],
    "students": [100, 80, 60, 40, 20]
})

sns.barplot(data=df, x="programming_language", y="students", palette="viridis") # x-axis => programming_language, y-axis => students
plt.title('Number of Students Learning Programming Languages') # title of the chart
plt.show()

# Lesson Learned:
# - Seaborn is a powerful data visualization library built on top of Matplotlib.
# - It provides a high-level interface for creating attractive and informative statistical graphics.
# - It is especially useful for exploratory data analysis and data visualization tasks.