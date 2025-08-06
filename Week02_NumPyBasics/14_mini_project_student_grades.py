import numpy as np

np.random.seed(56)
students = np.array(["Ali", "Sara", "John", "Amina"])
grades = np.random.randint(50, 100, size=(4, 5))  # 4 students, 5 subjects

print("Grades:\n", grades)

# Average per student
avg_student = np.mean(grades, axis=1)
print(avg_student)
print("\nAverage Grades per Student:")
for i, avg in enumerate(avg_student):
    print(f"{students[i]}: {avg:.2f}")

# Average per subject
avg_subject = np.mean(grades, axis=0)
print("\nAverage Grades per Subject:", avg_subject)

# Highest scoring student
top_student = students[np.argmax(avg_student)]
print("\nTop Student:", top_student)