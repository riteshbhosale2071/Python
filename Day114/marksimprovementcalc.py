def marksimprovementcalc():
    previous_marks = float(input("Enter the previous marks: "))
    current_marks = float(input("Enter the current marks: "))

    improvement = current_marks - previous_marks
    improvement_percentage = (improvement / previous_marks) * 100

    print("Marks Improvement:", improvement)

    if improvement > 0:
        print("Improvement Percentage:", round(improvement_percentage, 2), "%")
    elif improvement < 0:
        print("Marks Decreased by:", round(abs(improvement_percentage), 2), "%")
    else:
        print("No Change in Marks")

marksimprovementcalc()