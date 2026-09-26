import pandas as pd
from sklearn.linear_model import LinearRegression


data = {
    "area": [600, 900, 1100, 1300, 1600, 1900, 2100, 2400, 2700, 3200],
    "price": [1500000, 2200000, 2800000, 3300000, 4100000,
              4800000, 5300000, 6100000, 6800000, 8000000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


X = df[["area"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)


area = float(input("\nEnter house area in sq. ft.: "))


new_house = pd.DataFrame({"area": [area]})
prediction = model.predict(new_house)

print("Predicted House Price:", round(prediction[0], 2))