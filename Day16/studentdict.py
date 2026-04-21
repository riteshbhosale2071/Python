marks = {
    "Math": 80,
    "Science": 75,
    "English": 85,
    "Computer": 90
}
total = 0
for subject in marks:
    total += marks[subject]
average = total / len(marks)
print("Average marks:", average)