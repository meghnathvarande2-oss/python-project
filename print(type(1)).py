
import numpy as np

# Input number of students and subjects
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

# Input student names
students = []
for i in range(n):
    name = input(f"Enter name of Student {i + 1}: ")
    students.append(name)

# Input subject names
subjects = []
for j in range(m):
    subject = input(f"Enter name of Subject {j + 1}: ")
    subjects.append(subject)

# Input marks
marks = np.zeros((n, m), dtype=int)

for i in range(n):
    print(f"\nEnter marks for {students[i]}:")
    for j in range(m):
        marks[i][j] = int(input(f"{subjects[j]}: "))

# Calculate performance
total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)
minimum = np.min(marks, axis=1)
maximum = np.max(marks, axis=1)

# Display student report
print("\n===== STUDENT PERFORMANCE REPORT =====")

for i in range(n):
    print(f"\nStudent Name: {students[i]}")
    print("Marks:", marks[i])
    print("Total Marks:", total[i])
    print("Average Marks:", round(average[i], 2))
    print("Minimum Marks:", minimum[i])
    print("Maximum Marks:", maximum[i])

# Find top performer(s)
highest_total = np.max(total)
top_indices = np.where(total == highest_total)[0]

print("\n===== TOP PERFORMER =====")
for i in top_indices:
    print("Name:", students[i])
    print("Total Marks:", total[i])
    print("Average Marks:", round(average[i], 2))
