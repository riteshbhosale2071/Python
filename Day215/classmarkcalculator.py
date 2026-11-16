def classmarkcalculator():
    print("Class Mark Calculator")

    n = int(input("Enter the number of class intervals: "))

    if n <= 0:
        print("Please enter a positive number of intervals.")
        return

    class_marks = []

    print("\nEnter the lower and upper limits of each class interval:")

    for i in range(n):
        print(f"\nClass Interval {i + 1}")
        lower = float(input("Enter lower limit: "))
        upper = float(input("Enter upper limit: "))

        if lower > upper:
            print("Invalid interval. Lower limit cannot exceed upper limit.")
            return

        class_mark = (lower + upper) / 2
        class_marks.append(class_mark)

        print(f"Class Mark: {class_mark:g}")

    print("\nClass Mark Table :")
    print(f"{'Class':<10}{'Class Mark':<15}")

    for i, mark in enumerate(class_marks, start=1):
        print(f"{i:<10}{mark:<15g}")

classmarkcalculator()