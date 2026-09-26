
import pandas as pd


names = []
roll_numbers = []
marks = []
attendance = []


for i in range(3):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    mark = float(input("Enter marks: "))
    attend = float(input("Enter attendance (%): "))

    names.append(name)
    roll_numbers.append(roll)
    marks.append(mark)
    attendance.append(attend)


df = pd.DataFrame({
    "student_name": names,
    "roll_number": roll_numbers,
    "marks": marks,
    "attendance": attendance
})


print("\nComplete Student Data")
print(df)


result = df[df["marks"] > 80]


print("\nStudents Scoring Above 80")
print(result)