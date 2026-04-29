import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# =============================================================
#  MY FIRST PROJECT
# =============================================================

# Step 1: =>  Load the dataset

df = pd.read_csv('data_files/student_performance.csv')
'''
print(df.head())
print(df.shape) # (1000, 8) => 1000 rows and 8 columns
print(df.columns.tolist()) 
'''

# Step 2: =>  Inspection of the data
'''
print("\n== DATA TYPES == & MISSING VALUES ==")
print(df.info())


print("\n== STATISTICAL SUMMARY ==")
print(df.describe())
'''

'''
print("\n== MISSING VALUES PER COLUMN ==")
print(df.isnull().sum())
'''

'''
print("\n== CATEGORICAL COLUMNS - UNIQUE VALUES ==")
print("Gender:", df['gender'].unique())
print("Race:", df['race_ethnicity'].unique())
print("Education:", df['parental_education'].unique())
print("Lunch:", df['lunch'].unique())
print("Test Prep:", df['test_preparation'].unique())
'''


# Step 3: =>  Data Cleaning

# Add a new column for the average score of each student

df['average_score'] = (df['math_score'] + df['reading_score'] + df['writing_score']) / 3

# Add a new column to classify students as 'Pass' or 'Fail' based on their average score
# Assuming a passing threshold of 50 for the average score

df['pass_fail'] = df['average_score'].apply(lambda x: 'Pass' if x >= 50 else 'Fail') # 50 is the passing threshold for the average score

# Check the results of the new columns
print(df[['math_score', 'reading_score', 'writing_score', 'average_score', 'pass_fail']].head(10))


# How many passed vs failed?
print("\n=== PASS/FAIL BREAKDOWN ===")
print(df['pass_fail'].value_counts())
print(df['pass_fail'].value_counts(normalize=True).mul(100).round(1))




# Step 4: =>  Exploratory Data Analysis (EDA)

# === FACTOR 1: GENDER ===
print("=== AVERAGE SCORES BY GENDER ===")

# group the data by gender and calculate the mean of the scores for each gender

print(df.groupby('gender')[['math_score',
                             'reading_score',
                             'writing_score',
                             'average_score']].mean().round(2))

# === FACTOR 2: LUNCH TYPE (INCOME PROXY) ===
print("\n=== AVERAGE SCORES BY LUNCH TYPE ===")

# group the data by lunch type and calculate the mean of the scores for each lunch type

print(df.groupby('lunch')[['math_score','reading_score','writing_score','average_score']].mean().round(2))

# === FACTOR 3: TEST PREPARATION ===
print("\n=== AVERAGE SCORES BY TEST PREPARATION ===")

# group the data by test preparation and calculate the mean of the scores for each test preparation status

print(df.groupby('test_preparation')[['math_score',
                                       'reading_score',
                                       'writing_score',
                                       'average_score']].mean().round(2))

# === FACTOR 4: PARENTAL EDUCATION ===
print("\n=== AVERAGE SCORES BY PARENTAL EDUCATION ===")

# group the data by parental education and calculate the mean of the scores for each parental education level, then sort by average score in descending order
print(df.groupby('parental_education')[['average_score']]
      .mean().round(2).sort_values('average_score', ascending=False))





print("\n=== DIFFERENCE BETWEEN STANDARD AND FREE/REDUCED LUNCH ===")

# Is the difference between standard and free/reduced lunch REAL
# or could it be random chance?

standard = df[df['lunch'] == 'standard']['average_score']
reduced  = df[df['lunch'] == 'free/reduced']['average_score']

t_stat, p_value = stats.ttest_ind(standard, reduced)

print(f"Standard lunch mean:      {standard.mean():.2f}")
print(f"Free/reduced lunch mean:  {reduced.mean():.2f}")
print(f"Difference:               {standard.mean() - reduced.mean():.2f} points")
print(f"P-value:                  {p_value:.6f}")

if p_value < 0.05:
    print("CONCLUSION: This difference is statistically significant.")
    print("The income gap in performance is REAL, not random chance.")
else:
    print("CONCLUSION: Not statistically significant.")
    
    
    
    
    
    # Set the overall style
sns.set_style("whitegrid")
fig = plt.figure(figsize=(16, 12))
fig.suptitle("Student Performance Analysis — Key Findings", 
             fontsize=16, fontweight='bold', y=1.02)

# ── CHART 1: Average score by gender ──
ax1 = fig.add_subplot(2, 3, 1)
gender_scores = df.groupby('gender')['average_score'].mean()
colors = ['#2E86AB', '#E84855']
gender_scores.plot(kind='bar', ax=ax1, color=colors, 
                   edgecolor='black', width=0.5)
ax1.set_title('Average Score by Gender', fontweight='bold')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Average Score')
ax1.set_ylim(60, 85)
ax1.tick_params(axis='x', rotation=0)
for i, v in enumerate(gender_scores):
    ax1.text(i, v + 0.3, f'{v:.1f}', ha='center', 
             fontweight='bold', fontsize=11)

# ── CHART 2: Average score by lunch type ──
ax2 = fig.add_subplot(2, 3, 2)
lunch_scores = df.groupby('lunch')['average_score'].mean()
colors2 = ['#F18F01', '#2E86AB']
lunch_scores.plot(kind='bar', ax=ax2, color=colors2, 
                  edgecolor='black', width=0.5)
ax2.set_title('Average Score by Lunch Type\n(Income Proxy)', 
              fontweight='bold')
ax2.set_xlabel('Lunch Type')
ax2.set_ylabel('Average Score')
ax2.set_ylim(60, 85)
ax2.tick_params(axis='x', rotation=15)
for i, v in enumerate(lunch_scores):
    ax2.text(i, v + 0.3, f'{v:.1f}', ha='center', 
             fontweight='bold', fontsize=11)

# ── CHART 3: Average score by test preparation ──
ax3 = fig.add_subplot(2, 3, 3)
prep_scores = df.groupby('test_preparation')['average_score'].mean()
colors3 = ['#E84855', '#3BB273']
prep_scores.plot(kind='bar', ax=ax3, color=colors3, 
                 edgecolor='black', width=0.5)
ax3.set_title('Average Score by Test Preparation', fontweight='bold')
ax3.set_xlabel('Test Preparation')
ax3.set_ylabel('Average Score')
ax3.set_ylim(60, 88)
ax3.tick_params(axis='x', rotation=15)
for i, v in enumerate(prep_scores):
    ax3.text(i, v + 0.3, f'{v:.1f}', ha='center', 
             fontweight='bold', fontsize=11)

# ── CHART 4: Parental education vs average score ──
ax4 = fig.add_subplot(2, 3, 4)
edu_order = ['some high school', 'high school', 'some college',
             'associate degree', 'bachelor degree', 'master degree']
edu_scores = df.groupby('parental_education')['average_score']\
               .mean().reindex(edu_order)
edu_scores.plot(kind='bar', ax=ax4, color='#7B2D8B', 
                edgecolor='black', width=0.6)
ax4.set_title('Average Score by Parental Education', fontweight='bold')
ax4.set_xlabel('Parental Education')
ax4.set_ylabel('Average Score')
ax4.set_ylim(60, 88)
ax4.tick_params(axis='x', rotation=30, labelsize=8)
for i, v in enumerate(edu_scores):
    ax4.text(i, v + 0.3, f'{v:.1f}', ha='center', 
             fontweight='bold', fontsize=9)

# ── CHART 5: Distribution of average scores ──
ax5 = fig.add_subplot(2, 3, 5)
ax5.hist(df['average_score'], bins=30, color='#2E86AB', 
         edgecolor='black', alpha=0.8)
ax5.axvline(df['average_score'].mean(), color='red', 
            linestyle='--', linewidth=2, label=f'Mean: {df["average_score"].mean():.1f}')
ax5.axvline(df['average_score'].median(), color='green', 
            linestyle='--', linewidth=2, label=f'Median: {df["average_score"].median():.1f}')
ax5.set_title('Distribution of Average Scores', fontweight='bold')
ax5.set_xlabel('Average Score')
ax5.set_ylabel('Number of Students')
ax5.legend()

# ── CHART 6: Score comparison by subject and lunch type ──
ax6 = fig.add_subplot(2, 3, 6)
subjects = ['math_score', 'reading_score', 'writing_score']
lunch_subject = df.groupby('lunch')[subjects].mean()
x = np.arange(len(subjects))
width = 0.35
bars1 = ax6.bar(x - width/2, lunch_subject.loc['standard'], 
                width, label='Standard', color='#3BB273', edgecolor='black')
bars2 = ax6.bar(x + width/2, lunch_subject.loc['free/reduced'], 
                width, label='Free/Reduced', color='#E84855', edgecolor='black')
ax6.set_title('Scores by Subject & Lunch Type', fontweight='bold')
ax6.set_xlabel('Subject')
ax6.set_ylabel('Average Score')
ax6.set_xticks(x)
ax6.set_xticklabels(['Math', 'Reading', 'Writing'])
ax6.set_ylim(60, 88)
ax6.legend()

plt.tight_layout()
plt.savefig('student_analysis_charts.png', dpi=150, bbox_inches='tight')
plt.show()
print("Charts saved as student_analysis_charts.png")