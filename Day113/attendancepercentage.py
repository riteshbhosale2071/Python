def attendancepercentage():
    total_classes = int(input("Enter total classes held: "))
    attended_classes = int(input("Enter classes attended: "))

    percentage = (attended_classes / total_classes) * 100

    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Attendance Status: Eligible")
    else:
        print("Attendance Status: Short Attendance")

attendancepercentage()