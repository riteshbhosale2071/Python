students = [("Ritesh", 85), ("Amit", 70), ("Neha", 90), ("Karan", 75)]
print(students)
students.sort(key=lambda x: x[1])
print(students)