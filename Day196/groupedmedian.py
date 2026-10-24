def groupedmedian():
    print("Grouped Median Estimator :")

    try:
        n = int(input("Enter the number of class intervals: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of class intervals must be greater than zero.")
        return

    classes = []
    frequencies = []

    for i in range(n):
        print("\nClass Interval", i + 1)

        try:
            lower = float(input("Enter lower class limit: "))
            upper = float(input("Enter upper class limit: "))
            frequency = int(input("Enter frequency: "))
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")
            return

        if lower >= upper:
            print("Upper limit must be greater than lower limit.")
            return

        if frequency < 0:
            print("Frequency cannot be negative.")
            return

        classes.append((lower, upper))
        frequencies.append(frequency)

    for i in range(1, n):
        if classes[i][0] < classes[i - 1][0]:
            print("Class intervals must be entered in ascending order.")
            return

        if classes[i][0] < classes[i - 1][1]:
            print("Class intervals must not overlap.")
            return

    total_frequency = sum(frequencies)

    if total_frequency == 0:
        print("Median cannot be estimated because total frequency is zero.")
        return

    cumulative_frequencies = []
    cumulative_total = 0

    for frequency in frequencies:
        cumulative_total += frequency
        cumulative_frequencies.append(cumulative_total)

    median_position = total_frequency / 2
    median_class_index = -1

    for i in range(n):
        if cumulative_frequencies[i] >= median_position:
            median_class_index = i
            break

    lower_limit, upper_limit = classes[median_class_index]
    median_class_frequency = frequencies[median_class_index]

    if median_class_frequency == 0:
        print("Median class has zero frequency; estimation is not possible.")
        return

    if median_class_index == 0:
        previous_cumulative_frequency = 0
    else:
        previous_cumulative_frequency = cumulative_frequencies[
            median_class_index - 1
        ]

    class_width = upper_limit - lower_limit

    median = lower_limit + (
        (median_position - previous_cumulative_frequency)
        / median_class_frequency
    ) * class_width

    print("\nGrouped Frequency Table :")
    print("{:<20}{:<15}{:<20}".format(
        "Class Interval", "Frequency", "Cumulative Frequency"
    ))
    print("-" * 55)

    for i in range(n):
        lower, upper = classes[i]
        interval = str(lower) + " - " + str(upper)

        print("{:<20}{:<15}{:<20}".format(
            interval,
            frequencies[i],
            cumulative_frequencies[i]
        ))

    print("-" * 55)

    print("\nMedian Calculation :")
    print("Total Frequency (N):", total_frequency)
    print("N / 2:", median_position)
    print("Median Class:", classes[median_class_index])
    print("Lower Class Limit (L):", lower_limit)
    print("Cumulative Frequency Before Median Class:",
          previous_cumulative_frequency)
    print("Median Class Frequency (f):", median_class_frequency)
    print("Class Width (h):", class_width)

    print("\nFormula:")
    print("Median = L + ((N/2 - CF) / f) * h")

    print("Estimated Median:", round(median, 4))

    print("\nVerification :")
    print("Total of Frequencies:", sum(frequencies))
    print("Final Cumulative Frequency:", cumulative_frequencies[-1])

    if sum(frequencies) == cumulative_frequencies[-1]:
        print("Verification successful: Frequencies are consistent.")
    else:
        print("Verification failed: Check the frequency table.")

    print("\nNote: The median is estimated using the grouped-data formula.")

groupedmedian()