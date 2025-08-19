import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

segments = ['Low', 'Medium', 'High', 'VIP']

data = {
    'Customer Segment': np.repeat(segments, 200),
    'Purchase Amount': np.concatenate([
        np.random.gamma(shape=2, scale=50, size=200),
        np.random.normal(loc=150, scale=30, size=200),
        np.random.normal(loc=200, scale=50, size=200),
        np.random.normal(loc=300, scale=100, size=200)
    ])
}

df = pd.DataFrame(data)
sns.set_theme(style="whitegrid")
sns.set_context("talk")
plt.figure(figsize=(8, 8))

# Create the boxplot
sns.boxplot(
    x='Customer Segment',
    y='Purchase Amount',
    data=df,
    palette='Set2'
)

# Add title and axis labels with formatting
plt.title('Purchase Amount Distribution by Customer Segment', fontsize=16, weight='bold')
plt.xlabel('Customer Segment', fontsize=14)
plt.ylabel('Purchase Amount ($)', fontsize=14)

# Save the plot as PNG with exact size
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()