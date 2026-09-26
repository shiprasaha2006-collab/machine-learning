import pandas as pd
import numpy as np


data = {
    "age": [21, 24, 27, 32, 36, 41, 46, 52],
    "salary": [22000, 28000, 33000, 42000, 48000, 58000, 68000, 85000],
    "department": ["IT", "HR", "Marketing", "Finance", "IT", "HR", "Sales", "IT"],
    "years_of_experience": [0, 2, 3, 6, 9, 13, 17, 22]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


df.loc[1, "age"] = np.nan
df.loc[3, "salary"] = np.nan
df.loc[5, "department"] = np.nan
df.loc[6, "years_of_experience"] = np.nan

print("\nDataset with Missing Values:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())
df["years_of_experience"] = df["years_of_experience"].fillna(
    df["years_of_experience"].median()
)


df["department"] = df["department"].fillna(df["department"].mode()[0])

print("\nPreprocessed Dataset:")
print(df)