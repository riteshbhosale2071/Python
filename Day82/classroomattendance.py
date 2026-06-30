def attendance():
    total_students = int(input("Enter total number of students: "))

    present = 0
    absent = 0

    for i in range(total_students):
        status = input(f"Enter attendance for Student {i+1} (P/A): ").upper()

        if status == "P":
            present += 1
        elif status == "A":
            absent += 1
        else:
            print("Invalid input!")

    attendance_percentage = (present / total_students) * 100

    print("\nAttendance Report")
    print("-------------------------")
    print("Total Students :", total_students)
    print("Present Students :", present)
    print("Absent Students :", absent)
    print("Attendance Percentage :", round(attendance_percentage, 2), "%")

attendance()