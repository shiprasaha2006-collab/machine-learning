import pandas as pd
from sklearn.linear_model import LogisticRegression

n = int(input("Enter number of students: "))

study_hours = []
attendance = []
result = []


for i in range(n):
    print(f"\nStudent {i+1}")
    study_hours.append(float(input("Enter study hours: ")))
    attendance.append(float(input("Enter attendance (%): ")))
    result.append(int(input("Enter result (1=Pass, 0=Fail): ")))

df = pd.DataFrame({
    "Study_Hours": study_hours,
    "Attendance": attendance,
    "Pass": result
})

print("\nStudent Dataset:")
print(df)


X = df[["Study_Hours", "Attendance"]]
y = df["Pass"]

model = LogisticRegression()
model.fit(X, y)


print("\nEnter details of a new student:")
hours = float(input("Enter study hours: "))
att = float(input("Enter attendance (%): "))

prediction = model.predict([[hours, att]])

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")