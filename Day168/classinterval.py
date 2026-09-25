def classinterval():
    print("Class Interval Generator :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    minimum = min(values)
    maximum = max(values)

    class_width = float(input("Enter class width: "))

    if class_width <= 0:
        print("Class width must be greater than zero.")
        return

    number_of_classes = int((maximum - minimum) / class_width) + 1

    print("\nClass Intervals :")

    lower_limit = minimum

    for i in range(number_of_classes):
        upper_limit = lower_limit + class_width

        print(
            "Class", i + 1, ":",
            round(lower_limit, 2),
            "to",
            round(upper_limit, 2)
        )

        lower_limit = upper_limit

    print("\nMinimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Class Width:", class_width)
    print("Number of Classes:", number_of_classes)

classinterval()