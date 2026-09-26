import pandas as pd


n = int(input("Enter number of students: "))

names = []
roll_numbers = []
marks = []


for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    mark = float(input("Enter marks: "))

    names.append(name)
    roll_numbers.append(roll)
    marks.append(mark)


df = pd.DataFrame({
    "student_name": names,
    "roll_number": roll_numbers,
    "marks": marks
})


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


df["grade"] = df["marks"].apply(calculate_grade)


print("\nFinal DataFrame:")
print(df)