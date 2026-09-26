import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


np.random.seed(42)

area = np.linspace(500, 3500, 100)

price = 2000 + 50 * area + 0.05 * (area ** 2) + np.random.randn(100) * 20000

df = pd.DataFrame({'area': area, 'price': price})

X_train, X_test, y_train, y_test = train_test_split(
    df[['area']], df['price'], test_size=0.2, random_state=42
)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)

r2_lin = r2_score(y_test, y_pred_lin)
print("Linear Regression R^2:", r2_lin)


poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
y_pred_poly = poly_reg.predict(X_test_poly)

r2_poly = r2_score(y_test, y_pred_poly)
print("Polynomial Regression R^2:", r2_poly)

plt.scatter(df['area'], df['price'], color='blue', label='Actual Data')

plt.plot(X_test, y_pred_lin, color='red', linewidth=2, label='Linear Regression')


X_range = pd.DataFrame({'area': np.linspace(500, 3500, 200)})
plt.plot(X_range, poly_reg.predict(poly.transform(X_range)), 
         color='green', linewidth=2, label='Polynomial Regression')

plt.xlabel("Area (sq. ft)")
plt.ylabel("Price (INR)")
plt.title("House Price Prediction: Linear vs Polynomial Regression")
plt.legend()
plt.show()
