def performance():
    n = int(input("Enter number of students: "))

    marks = []

    for i in range(n):
        mark = int(input(f"Enter marks of Student {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / n

    excellent = 0
    good = 0
    average_students = 0
    fail = 0

    for mark in marks:
        if mark >= 75:
            excellent += 1
        elif mark >= 50:
            good += 1
        elif mark >= 35:
            average_students += 1
        else:
            fail += 1

    print("\nClass Performance Report")
    print("-" * 35)
    print("Highest Marks =", max(marks))
    print("Lowest Marks =", min(marks))
    print("Total Marks =", total)
    print("Average Marks =", round(average, 2))
    print("Excellent Students =", excellent)
    print("Good Students =", good)
    print("Average Students =", average_students)
    print("Failed Students =", fail)

performance()