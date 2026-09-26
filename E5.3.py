import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

n = int(input("Enter number of students: "))

study_hours = []
attendance = []
result = []


for i in range(n):
    print(f"\nStudent {i + 1}")

    hours = float(input("Enter study hours: "))
    att = float(input("Enter attendance (%): "))
    res = int(input("Enter result (1=Pass, 0=Fail): "))

    study_hours.append(hours)
    attendance.append(att)
    result.append(res)

df = pd.DataFrame({
    "Study_Hours": study_hours,
    "Attendance": attendance,
    "Pass": result
})

print("\nDataset:")
print(df)

X = df[["Study_Hours", "Attendance"]]
y = df["Pass"]

model = LogisticRegression()
model.fit(X, y)

y_probability = model.predict_proba(X)[:, 1]

fpr, tpr, thresholds = roc_curve(y, y_probability)

auc_score = roc_auc_score(y, y_probability)

print("\nAUC Score:", round(auc_score, 3))


plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {auc_score:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()