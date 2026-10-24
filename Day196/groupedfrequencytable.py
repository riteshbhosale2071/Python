def groupedfrequencytable():
    print("Grouped Frequency Table :")

    try:
        n = int(input("Enter the number of data values: "))

        if n <= 0:
            print("Number of data values must be greater than zero.")
            return

        data = []

        for i in range(n):
            value = float(input("Enter data value " + str(i + 1) + ": "))
            data.append(value)

        class_width = float(input("Enter the class interval width: "))

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if class_width <= 0:
        print("Class interval width must be greater than zero.")
        return

    minimum = min(data)
    maximum = max(data)

    start = int(minimum // class_width) * class_width
    end = int(maximum // class_width) * class_width

    if maximum == end:
        end -= class_width

    classes = []
    frequencies = []

    lower = start

    while lower <= maximum:
        upper = lower + class_width
        frequency = 0

        for value in data:
            if lower <= value < upper:
                frequency += 1

        classes.append((lower, upper))
        frequencies.append(frequency)
        lower = upper

    print("\nGrouped Frequency Table :")
    print("{:<20}{:<15}{:<20}".format(
        "Class Interval", "Frequency", "Cumulative Frequency"
    ))
    print("-" * 55)

    cumulative_frequency = 0

    for i in range(len(classes)):
        lower, upper = classes[i]
        frequency = frequencies[i]
        cumulative_frequency += frequency

        interval = str(round(lower, 2)) + " - " + str(round(upper, 2))

        print("{:<20}{:<15}{:<20}".format(
            interval, frequency, cumulative_frequency
        ))

    print("-" * 55)
    print("Total Data Values:", n)
    print("Total Frequency:", sum(frequencies))
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Class Width:", class_width)

    print("\nFrequency Verification :")

    if sum(frequencies) == len(data):
        print("Verification successful: All data values are counted.")
    else:
        print("Warning: Some data values may not have been counted.")

    print("\nRelative Frequency :")
    for i in range(len(classes)):
        lower, upper = classes[i]
        relative_frequency = frequencies[i] / n
        percentage = relative_frequency * 100

        print(
            str(round(lower, 2)) + " - " + str(round(upper, 2)),
            "| Frequency:", frequencies[i],
            "| Relative Frequency:", round(relative_frequency, 4),
            "| Percentage:", round(percentage, 2), "%"
        )

groupedfrequencytable()