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
        np.random.normal(loc=300, scale=100, size=200),
    ])
}
df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")
sns.set_context("talk")

# EXACT 512x512 canvas
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)  # 8" * 64 dpi = 512 px
sns.boxplot(x='Customer Segment', y='Purchase Amount', data=df, palette='Set2', ax=ax)

ax.set_title('Purchase Amount Distribution by Customer Segment', fontsize=16, weight='bold')
ax.set_xlabel('Customer Segment', fontsize=14)
ax.set_ylabel('Purchase Amount ($)', fontsize=14)

fig.tight_layout()  # adjusts margins but does NOT change 512x512 canvas
fig.savefig('chart.png')  # no bbox_inches='tight'
plt.close(fig)
