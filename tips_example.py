import seaborn as sns  # pandas as pd - is not used but DataFrames are created.
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# Data cleaning/transformation
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips['size_squared'] = np.square(tips['size'])

# Aggregation/analysis
avg_tip_pct_by_day = tips.groupby('day')['tip_pct'].mean()

# Visualization
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_tip_pct_by_day.index, y=avg_tip_pct_by_day.values)
plt.title('Average Tip Percentage by Day')
plt.show()


def test_tips_load():
    tips = sns.load_dataset('tips')
    assert tips.size > 0


def test_np_access():
    tips = sns.load_dataset('tips')
    tips['size_squared'] = np.square(tips['size'])
    assert tips['size_squared'].size > 0
