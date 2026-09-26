import numpy as np
import pandas as pd

np.random.seed(42)

# Features
area = np.linspace(500, 2500, 100)                 
bedrooms = np.random.randint(1, 4, size=100)       
bathrooms = np.random.randint(1, 3, size=100)      
age = np.random.randint(1, 20, size=100)          

price = (500 
         + 20 * area 
         + 50000 * bedrooms 
         + 30000 * bathrooms 
         - 2000 * age 
         + np.random.randn(100) * 5000)

df = pd.DataFrame({
    'area': area,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'age': age,
    'price': price
})

print(df.head())
