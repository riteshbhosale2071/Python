def reportcard():
    student_name = input("Enter student name: ")

    english = int(input("Enter English marks: "))
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    social = int(input("Enter Social marks: "))
    computer = int(input("Enter Computer marks: "))

    total = english + maths + science + social + computer
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 35:
        grade = "C"
    else:
        grade = "F"

    print("\nMini Report Card")
    print("-" * 30)
    print("Student Name :", student_name)
    print("English :", english)
    print("Maths :", maths)
    print("Science :", science)
    print("Social :", social)
    print("Computer :", computer)
    print("Total Marks :", total)
    print("Average Marks :", round(average, 2))
    print("Grade :", grade)

reportcard()