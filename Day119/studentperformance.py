def studentperformance():
    marks1 = float(input("Enter marks in Subject 1: "))
    marks2 = float(input("Enter marks in Subject 2: "))
    marks3 = float(input("Enter marks in Subject 3: "))

    total = marks1 + marks2 + marks3
    average = total / 3

    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 50:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

studentperformance()