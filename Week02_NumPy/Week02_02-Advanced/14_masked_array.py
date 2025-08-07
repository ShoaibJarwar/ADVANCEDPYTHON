import numpy as np
import numpy.ma as ma

# Simulated grades with missing values (-1 represents missing)
grades = np.array([
    [87, 92, 78, -1, 90],
    [91, -1, 95, 92, 88],
    [70, 75, 80, 72, 78],
    [88, 84, -1, 86, 87]
])

students = np.array(["Ali", "Sara", "John", "Amina"])

# Mask grades that are -1
masked_grades = ma.masked_where(grades == -1, grades)

print("Masked Grades:\n", masked_grades)

# Average per student (ignoring masked values)
avg_student = masked_grades.mean(axis=1)

print("\nAverage Grades per Student (ignoring missing values):")
for i, avg in enumerate(avg_student):
    print(f"{students[i]}: {avg:.2f}")