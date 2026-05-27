import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('data_files/covid_africa.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns.tolist())
print(df.shape)



# Sort by country and date first — critical for cumulative calculation
df = df.sort_values(['country', 'date']).reset_index(drop=True)

# Add cumulative columns per country
df['cumulative_cases']  = df.groupby('country')['daily_cases'].cumsum()
df['cumulative_deaths'] = df.groupby('country')['daily_deaths'].cumsum()

# Add mortality rate column
df['mortality_rate'] = (df['daily_deaths'] / df['daily_cases'].replace(0, 1) * 100).round(2)

print(df[['country','date','daily_cases','cumulative_cases','mortality_rate']].head(20))


# Total burden per country
country_summary = df.groupby('country').agg(
    total_cases  = ('daily_cases', 'sum'),
    total_deaths = ('daily_deaths', 'sum'),
    peak_cases   = ('daily_cases', 'max'), 
    avg_daily    = ('daily_cases', 'mean')
).round(0).sort_values('total_cases', ascending=False)

print(country_summary)


# Mortality rate per country
mortality = df.groupby('country').agg(
    total_cases  = ('daily_cases', 'sum'),
    total_deaths = ('daily_deaths', 'sum')
)
mortality['mortality_rate_%'] = (
    mortality['total_deaths'] / mortality['total_cases'] * 100
).round(2)

print(mortality.sort_values('mortality_rate_%', ascending=False))


# How did cases change year by year?
yearly = df.groupby(['country', 'year'])['daily_cases'].sum().unstack()
print(yearly)

# Percentage change from 2020 to 2021
yearly['change_2020_to_2021_%'] = (
    (yearly[2021] - yearly[2020]) / yearly[2020] * 100
).round(1)

print("\nYear on year change:")
print(yearly[['change_2020_to_2021_%']].sort_values(
    'change_2020_to_2021_%', ascending=False))

sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('COVID-19 in Africa — Trend Analysis',
             fontsize=16, fontweight='bold')

# ── CHART 1: Daily cases over time for all countries ──
ax1 = axes[0, 0]
for country in df['country'].unique():
    country_data = df[df['country'] == country]
    ax1.plot(country_data['date'],
             country_data['daily_cases'],
             label=country, linewidth=1.5)
ax1.set_title('Daily Cases Over Time by Country', fontweight='bold')
ax1.set_xlabel('Date')
ax1.set_ylabel('Daily Cases')
ax1.legend(fontsize=8)
ax1.tick_params(axis='x', rotation=45)

# ── CHART 2: Total cases by country (bar) ──
ax2 = axes[0, 1]
total_by_country = df.groupby('country')['daily_cases'].sum()\
                     .sort_values(ascending=False)
colors = sns.color_palette('Blues_d', len(total_by_country))
bars = ax2.bar(total_by_country.index, total_by_country.values,
               color=colors, edgecolor='black')
ax2.set_title('Total Cases by Country', fontweight='bold')
ax2.set_xlabel('Country')
ax2.set_ylabel('Total Cases')
ax2.tick_params(axis='x', rotation=45)
for bar, val in zip(bars, total_by_country.values):
    ax2.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 5000,
             f'{val:,.0f}', ha='center', fontsize=8)

# ── CHART 3: Mortality rate by country ──
ax3 = axes[1, 0]
mortality_rate = (df.groupby('country')['daily_deaths'].sum() /
                  df.groupby('country')['daily_cases'].sum() * 100)\
                   .sort_values(ascending=False)
colors2 = sns.color_palette('Reds_d', len(mortality_rate))
bars2 = ax3.bar(mortality_rate.index, mortality_rate.values,
                color=colors2, edgecolor='black')
ax3.set_title('Mortality Rate by Country (%)', fontweight='bold')
ax3.set_xlabel('Country')
ax3.set_ylabel('Mortality Rate (%)')
ax3.tick_params(axis='x', rotation=45)
for bar, val in zip(bars2, mortality_rate.values):
    ax3.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.05,
             f'{val:.2f}%', ha='center', fontsize=9)

# ── CHART 4: Cumulative cases for top 4 countries ──
ax4 = axes[1, 1]
top4 = total_by_country.head(4).index.tolist()
for country in top4:
    country_data = df[df['country'] == country]
    ax4.plot(country_data['date'],
             country_data['cumulative_cases'],
             label=country, linewidth=2)
ax4.set_title('Cumulative Cases — Top 4 Countries', fontweight='bold')
ax4.set_xlabel('Date')
ax4.set_ylabel('Cumulative Cases')
ax4.legend()
ax4.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('covid_africa_charts.png', dpi=150, bbox_inches='tight')
plt.show()
print("Charts saved")