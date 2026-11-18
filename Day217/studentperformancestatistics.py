def studentperformancestatistics():
    print("Student Performance Statistics :")

    n = int(input("Enter the number of students: "))

    if n <= 0:
        print("Please enter a positive number of students.")
        return

    students = []
    marks_list = []

    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        students.append((name, marks))
        marks_list.append(marks)

    average = sum(marks_list) / n
    highest = max(marks_list)
    lowest = min(marks_list)

    sorted_marks = sorted(marks_list)

    if n % 2 == 0:
        median = (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2
    else:
        median = sorted_marks[n // 2]

    passed = sum(1 for marks in marks_list if marks >= 35)
    failed = n - passed
    pass_percentage = (passed / n) * 100

    print("\nStudent Performance Report:")
    print(f"{'Student Name':<20}{'Marks':<10}{'Grade':<10}")

    for name, marks in students:
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 35:
            grade = "D"
        else:
            grade = "Fail"

        print(f"{name:<20}{marks:<10.2f}{grade:<10}")

    print("\nPerformance Statistics:")
    print("Total Students:", n)
    print("Average Marks:", round(average, 2))
    print("Median Marks:", round(median, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Passed Students:", passed)
    print("Failed Students:", failed)
    print("Pass Percentage:", round(pass_percentage, 2), "%")

    print("\nTop Performer:")
    for name, marks in students:
        if marks == highest:
            print(name, "-", marks)

studentperformancestatistics()