import numpy as np


marks = []

for i in range(10):
    mark = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)


marks = np.array(marks)


mean = np.mean(marks)
median = np.median(marks)
std = np.std(marks)
maximum = np.max(marks)
minimum = np.min(marks)


print("\nInternal Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Maximum:", maximum)
print("Minimum:", minimum)