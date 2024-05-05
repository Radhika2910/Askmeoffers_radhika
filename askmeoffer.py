import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Create a DataFrame with 1000 entries
data = {
    'user_id': np.random.randint(1, 501, 1000),  # 500 unique users
    'item_added_to_cart': np.random.choice([True, False], 1000, p=[0.7, 0.3]),
    'coupon_offered': np.random.choice(['Discount', 'BuyOneGetOne', 'None'], 1000, p=[0.4, 0.2, 0.4]),
    'coupon_used': np.random.choice([True, False], 1000, p=[0.5, 0.5]),
    'purchase_completed': np.random.choice([True, False], 1000, p=[0.6, 0.4])
}

df = pd.DataFrame(data)
print(df.head())

# Group by 'coupon_used' and calculate mean of 'purchase_completed'
purchase_rates = df.groupby('coupon_used')['purchase_completed'].mean()

# Display the purchase rates
print(purchase_rates)

# Perform a statistical test (e.g., Chi-squared test for independence)
from scipy.stats import chi2_contingency

# Create a contingency table
contingency_table = pd.crosstab(df['coupon_used'], df['purchase_completed'])

# Perform the Chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Display the p-value
print('P-value:', p_value)

