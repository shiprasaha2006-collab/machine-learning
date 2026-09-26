import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score

n = int(input("Enter number of students: "))

study_hours = []
attendance = []
result = []


for i in range(n):
    print(f"\nStudent {i+1}")

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


probability = model.predict_proba(X)[:, 1]


thresholds = [0.3, 0.5, 0.7]

print("\nThreshold | Precision | Recall")
print("--------------------------------")

for threshold in thresholds:

    
    y_pred = (probability >= threshold).astype(int)

    precision = precision_score(y, y_pred, zero_division=0)
    recall = recall_score(y, y_pred, zero_division=0)

    print(f"{threshold:^9} | {precision:.2f}      | {recall:.2f}")