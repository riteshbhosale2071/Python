def examscore():
    obtained_marks = float(input("Enter obtained marks: "))
    total_marks = float(input("Enter total marks: "))

    percentage = (obtained_marks / total_marks) * 100

    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 40:
        print("Grade: D")
    else:
        print("Grade: F")

examscore()