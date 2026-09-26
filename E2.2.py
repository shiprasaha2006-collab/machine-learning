import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine


wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)


plt.figure(figsize=(15, 10))


sns.boxplot(data=df, orient="h")

plt.title("Boxplots of Wine Dataset Numerical Attributes")
plt.xlabel("Value Range")
plt.ylabel("Attributes")
plt.show()
