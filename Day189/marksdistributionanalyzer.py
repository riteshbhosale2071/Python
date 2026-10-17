def marksdistributionanalyzer():
    print("Marks Distribution Analyzer :")

    n = int(input("Enter the number of students: "))

    if n <= 0:
        print("Number of students must be greater than zero.")
        return

    marks_list = []

    for i in range(n):
        marks = float(input("Enter marks for student " + str(i + 1) + " (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            return

        marks_list.append(marks)

    total_marks = sum(marks_list)
    average_marks = total_marks / n
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)

    grade_counts = {
        "A (90-100)": 0,
        "B (80-89.99)": 0,
        "C (70-79.99)": 0,
        "D (60-69.99)": 0,
        "E (40-59.99)": 0,
        "F (Below 40)": 0
    }

    passed = 0
    failed = 0

    for marks in marks_list:
        if marks >= 90:
            grade_counts["A (90-100)"] += 1
        elif marks >= 80:
            grade_counts["B (80-89.99)"] += 1
        elif marks >= 70:
            grade_counts["C (70-79.99)"] += 1
        elif marks >= 60:
            grade_counts["D (60-69.99)"] += 1
        elif marks >= 40:
            grade_counts["E (40-59.99)"] += 1
        else:
            grade_counts["F (Below 40)"] += 1

        if marks >= 40:
            passed += 1
        else:
            failed += 1

    print("\nMarks Distribution Summary :")
    print("Total Students:", n)
    print("Total Marks:", round(total_marks, 2))
    print("Average Marks:", round(average_marks, 2))
    print("Highest Marks:", highest_marks)
    print("Lowest Marks:", lowest_marks)
    print("Marks Range:", round(highest_marks - lowest_marks, 2))

    print("\nGrade Distribution :")
    for grade, count in grade_counts.items():
        percentage = (count / n) * 100
        print(grade + ":", count, "students (", round(percentage, 2), "%)")

    print("\nPass and Fail Analysis :")
    print("Passed Students:", passed)
    print("Failed Students:", failed)
    print("Pass Percentage:", round((passed / n) * 100, 2), "%")
    print("Fail Percentage:", round((failed / n) * 100, 2), "%")

    print("\nPerformance Evaluation :")

    if average_marks >= 80:
        print("Excellent overall performance!")
    elif average_marks >= 60:
        print("Good overall performance.")
    elif average_marks >= 40:
        print("Satisfactory overall performance.")
    else:
        print("Overall performance needs improvement.")

    print("\nSorted Marks :")
    print(sorted(marks_list, reverse=True))

marksdistributionanalyzer()