from scipy.stats import chi2_contingency
from scipy import stats
import numpy as np

# Rows = Gender (Male, Female)
# Columns = Provider (MTN, Vodafone, AirtelTigo)
observed = np.array([
    [120, 90, 60],   # Male
    [80,  110, 90]   # Female
])

chi2, p_value, dof, expected = chi2_contingency(observed)

print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("There IS a significant relationship between gender and provider preference")
else:
    print("There is NO significant relationship between gender and provider preference")
    
    
    
    
    


# Monthly savings BEFORE the SMS campaign
before = [1200, 1500, 1100, 1300, 1400, 1250, 1350, 1150, 1300, 1200]

# Monthly savings AFTER the SMS campaign
after  = [1500, 1800, 1400, 1600, 1700, 1550, 1650, 1450, 1600, 1500]

# Run the t-test
t_stat, p_value = stats.ttest_rel(before, after)

print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Result: Statistically significant — the campaign had a real effect")
else:
    print("Result: Not significant — could be random chance")