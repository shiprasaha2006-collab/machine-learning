import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine


wine = load_wine()


df = pd.DataFrame(wine.data, columns=wine.feature_names)


correlation = df.corr()


plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap of Wine Dataset")
plt.show()


corr_matrix = correlation.copy()


import numpy as np
np.fill_diagonal(corr_matrix.values, np.nan)

pair = corr_matrix.stack().idxmax()
value = corr_matrix.stack().max()

print("Strongest positive correlation:")
print(pair)
print("Correlation value:", value)