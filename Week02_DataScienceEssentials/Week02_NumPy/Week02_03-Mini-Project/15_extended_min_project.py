import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8') # To include emojis
import time
from collections import defaultdict


# Set seed for reproducibility
np.random.seed(35)

# Sample data
students = np.array(["Ali", "Maheen", "Sara", "Shoaib"])
subjects = np.array(["OOP", "PF", "Web Tech", "Visual Programming", "DSA"])
grades = np.random.randint(15, 60, size = (4, 5)) # 4 students, 5 subjects
 
print("🎓 Student Grades:\n", grades) 

# 1. Average per student
avg_student = np.mean(grades, axis=1)
print("\n📊 Average Grades per Student:")
for i, avg in enumerate(avg_student):
    print(f"{students[i]}: {avg:.2f}")
    
# 2. Average per subject 
avg_subject = np.mean(grades, axis=0)
print("\n📚 Average Grades per Subject:")
for i, avg in enumerate(avg_subject):
    print(f"{subjects[i]}: {avg:.2f}")

# 3. Highest scoring student
top_student = students[np.argmax(avg_student)]
print("\n🏅 Top Student:", top_student)

# 4. Fancy indexing: Get Maheen and Shoaib’s grades
selected_students = [1, 3]
selected_grades = grades[selected_students]
print("\n🎯 Grades for Maheen & Shoaib:\n", selected_grades)

# 5. Boolean masking: Students with average > 48
high_achievers = students[avg_student > 48]
print("\n🎖️ Students with Avg > 48:", high_achievers)

# 6. Broadcasting: Add 5 bonus marks in Web Tech to all students
grades_with_bonus = grades.copy()
grades_with_bonus[:, np.where(subjects == "Web Tech")[0][0]] += 5
# grades_with_bonus[:, subjects.tolist().index("Web Tech")] += 5
print("\n🎁 Grades after Adding Bonus in Web Tech:\n", grades_with_bonus)

# 7. Sorting: Students sorted by average grades (descending)
sorted_indices = np.argsort(avg_student)[::-1]
sorted_students = students[sorted_indices]
sorted_averages = avg_student[sorted_indices]

print("\n📈 Students Sorted by Average Grade:")
for i in range(len(students)):
    print(f"{sorted_students[i]}: {sorted_averages[i]:.2f}")

# 8. Axis-wise operations: Max grade per student
max_grades = np.max(grades, axis=1)
print("\n🔝 Highest Grade per Student:")
for i, grade in enumerate(max_grades):
    print(f"{students[i]}: {grade}")

# 9. Set operations: Students who passed all subjects (>= 24)
passed_all = np.all(grades >= 24, axis=1)
students_passed_all = students[passed_all]
print("\n✅ Students Who Passed All Subjects:", students_passed_all)

# 10. Which student failed in which subject
failed_subjects = defaultdict(list)
row, col = np.where(grades < 24)
for i in range(len(row)):
    student = students[row[i]]
    subject = subjects[col[i]]
    failed_subjects[student].append(subject)

for student, failed in failed_subjects.items():
    print(f"{student} failed in: {', '.join(failed)}")



# 11. Simple performance comparison (optional)
big_list = list(range(1000000))
start = time.time()
sum_list = sum(big_list)
end = time.time()
print("\n🕒 Python List Sum Time:", end - start)

big_array = np.arange(1000000)
start = time.time() 
sum_array = np.sum(big_array)
end = time.time()
print("⚡ NumPy Array Sum Time:", end - start)
