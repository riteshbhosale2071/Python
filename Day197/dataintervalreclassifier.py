def dataintervalreclassifier():
    print("Data Interval Reclassifier :")

    try:
        n = int(input("Enter the number of data values: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of data values must be greater than zero.")
        return

    data = []

    for i in range(n):
        try:
            value = float(input("Enter data value " + str(i + 1) + ": "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        data.append(value)

    try:
        class_width = float(input("\nEnter the new class interval width: "))
    except ValueError:
        print("Invalid class width!")
        return

    if class_width <= 0:
        print("Class interval width must be greater than zero.")
        return

    minimum = min(data)
    maximum = max(data)

    first_lower = (minimum // class_width) * class_width
    number_of_classes = int((maximum - first_lower) // class_width) + 1

    if abs(first_lower + number_of_classes * class_width - maximum) < 0.000001:
        number_of_classes += 1

    classes = []

    for i in range(number_of_classes):
        lower = first_lower + i * class_width
        upper = lower + class_width
        classes.append([lower, upper, 0])

    for value in data:
        index = int((value - first_lower) // class_width)

        if index >= len(classes):
            index = len(classes) - 1

        if value < classes[index][0] or value >= classes[index][1]:
            for j in range(len(classes)):
                if classes[j][0] <= value < classes[j][1]:
                    index = j
                    break

        classes[index][2] += 1

    print("\nReclassified Frequency Table :")
    print("{:<20}{:<20}{:<15}".format(
        "Class Interval", "Class Midpoint", "Frequency"
    ))
    print("-" * 55)

    total_frequency = 0
    cumulative_frequency = 0

    for lower, upper, frequency in classes:
        midpoint = (lower + upper) / 2
        cumulative_frequency += frequency
        total_frequency += frequency

        interval = str(round(lower, 2)) + " - " + str(round(upper, 2))

        print("{:<20}{:<20.2f}{:<15}".format(
            interval, midpoint, frequency
        ))

    print("-" * 55)
    print("Total Data Values:", len(data))
    print("Total Frequency:", total_frequency)
    print("Class Width:", class_width)
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Number of Classes:", len(classes))

    print("\nReclassification Verification :")

    if total_frequency == len(data):
        print("Verification successful: All data values are classified.")
    else:
        print("Verification failed: Some values may be missing.")

    print("\nCumulative Frequency :")

    cumulative_frequency = 0

    for lower, upper, frequency in classes:
        cumulative_frequency += frequency

        print(
            str(round(lower, 2)) + " - " + str(round(upper, 2)),
            "| Frequency:", frequency,
            "| Cumulative Frequency:", cumulative_frequency
        )

    print("\nData interval reclassification completed successfully.")

dataintervalreclassifier()