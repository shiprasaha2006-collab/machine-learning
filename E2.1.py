import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine


wine = load_wine()


df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["target"] = wine.target


print("First 5 rows:")
print(df.head())


print("\nShape:", df.shape)
print("\nInformation:")
print(df.info())


print("\nStatistical Summary:")
print(df.describe())


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Values:", df.duplicated().sum())


print("\nTarget Distribution:")
print(df["target"].value_counts())


df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
sns.boxplot(data=df.drop("target", axis=1))
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()