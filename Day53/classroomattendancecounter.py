def count():
    total_students = int(input("Enter total students: "))

    present_students = int(input("Enter present students: "))

    absent_students = total_students - present_students

    print("Present Students =", present_students)
    
    print("Absent Students =", absent_students)

count()