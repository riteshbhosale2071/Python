def setbasedstudentperformance():
    print("Set-Based Student Performance :")

    try:
        total_students = int(input("Enter the total number of students: "))
    except ValueError:
        print("Invalid input! Enter a valid integer.")
        return

    if total_students <= 0:
        print("The number of students must be greater than zero.")
        return

    all_students = set()
    passed_students = set()
    failed_students = set()
    distinction_students = set()

    for i in range(total_students):
        name = input("\nEnter student name: ").strip()

        if name == "":
            print("Student name cannot be empty.")
            return

        if name.lower() in {student.lower() for student in all_students}:
            print("Duplicate student name! Enter each student only once.")
            return

        try:
            marks = float(input("Enter marks out of 100: "))
        except ValueError:
            print("Invalid marks! Enter a numeric value.")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        all_students.add(name)

        if marks >= 40:
            passed_students.add(name)
        else:
            failed_students.add(name)

        if marks >= 75:
            distinction_students.add(name)

    print("\n" + "=" * 45)
    print("      STUDENT PERFORMANCE REPORT")
    print("=" * 45)

    print("\nAll Students:", sorted(all_students))
    print("Passed Students:", sorted(passed_students))
    print("Failed Students:", sorted(failed_students))
    print("Students with Distinction:", sorted(distinction_students))

    print("\nSet-Based Analysis :")

    print("Total Students:", len(all_students))
    print("Passed Students:", len(passed_students))
    print("Failed Students:", len(failed_students))
    print("Distinction Students:", len(distinction_students))

    print("\nStudents who passed but did not get distinction:")
    print(sorted(passed_students - distinction_students))

    print("\nStudents who failed or received distinction:")
    print(sorted(failed_students | distinction_students))

    print("\nStudents who are neither failed nor distinguished:")
    print(sorted(all_students - (failed_students | distinction_students)))

    print("\nChecking whether passed and failed sets are disjoint:")

    if passed_students.isdisjoint(failed_students):
        print("Yes, no student belongs to both sets.")
    else:
        print("No, some students appear in both sets.")

    print("\nChecking whether all students are accounted for:")

    if passed_students | failed_students == all_students:
        print("Verification successful.")
    else:
        print("Verification failed.")

    print("\nPass Percentage:",
          round(len(passed_students) / len(all_students) * 100, 2), "%")

    print("Failure Percentage:",
          round(len(failed_students) / len(all_students) * 100, 2), "%")

    print("\nStudent performance analysis completed successfully.")

setbasedstudentperformance()