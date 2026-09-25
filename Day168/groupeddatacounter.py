def groupeddatacounter():
    print("Grouped Data Counter :")

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

    lower_limit = minimum

    print("\nGrouped Data Frequency Table :")
    print("Class Interval\tFrequency")

    total_frequency = 0

    for i in range(number_of_classes):
        upper_limit = lower_limit + class_width
        frequency = 0

        for value in values:
            if i == number_of_classes - 1:
                if value >= lower_limit and value <= upper_limit:
                    frequency += 1
            else:
                if value >= lower_limit and value < upper_limit:
                    frequency += 1

        print(
            str(round(lower_limit, 2)) + " - " +
            str(round(upper_limit, 2)) + "\t\t" +
            str(frequency)
        )

        total_frequency += frequency
        lower_limit = upper_limit

    print("\nTotal Values:", number_of_values)
    print("Total Frequency:", total_frequency)

groupeddatacounter()