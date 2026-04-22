from scipy.stats import chi2_contingency
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