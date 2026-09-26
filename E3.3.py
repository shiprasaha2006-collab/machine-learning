import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler


data = np.array([[10],[20],[30],[40],[50]])


standard_scaler = StandardScaler()
standard_data = standard_scaler.fit_transform(data)


minmax_scaler = MinMaxScaler()
minmax_data = minmax_scaler.fit_transform(data)


print("Original Data:")
print(data)

print("\nStandardScaler Transformed Data:")
print(standard_data)

print("\nMinMaxScaler Transformed Data:")
print(minmax_data)


print("\nStandardScaler Range:")
print("Minimum:", standard_data.min())
print("Maximum:", standard_data.max())

print("\nMinMaxScaler Range:")
print("Minimum:", minmax_data.min())
print("Maximum:", minmax_data.max())