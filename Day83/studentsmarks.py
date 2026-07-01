def marks():
    n = int(input("Enter number of students: "))

    marks = []

    for i in range(n):
        mark = int(input(f"Enter marks of Student {i+1}: "))
        marks.append(mark)

    print("\nStudent Marks Report")
    print("-" * 30)

    print("Marks:", marks)
    print("Highest Marks =", max(marks))
    print("Lowest Marks =", min(marks))
    print("Total Marks =", sum(marks))
    print("Average Marks =", round(sum(marks) / n, 2))

    passed = 0
    failed = 0

    for mark in marks:
        if mark >= 35:
            passed += 1
        else:
            failed += 1

    print("Passed Students =", passed)
    print("Failed Students =", failed)

marks()