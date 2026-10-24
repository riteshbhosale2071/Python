def cumulativefrequencycalc():
    print("Cumulative Frequency Calculator :")

    try:
        n = int(input("Enter the number of classes: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of classes must be greater than zero.")
        return

    class_intervals = []
    frequencies = []

    for i in range(n):
        print("\nClass", i + 1)

        interval = input("Enter class interval (e.g., 0-10): ")

        try:
            frequency = int(input("Enter frequency: "))
        except ValueError:
            print("Invalid frequency! Please enter an integer.")
            return

        if frequency < 0:
            print("Frequency cannot be negative.")
            return

        class_intervals.append(interval)
        frequencies.append(frequency)

    cumulative_frequencies = []
    running_total = 0

    for frequency in frequencies:
        running_total += frequency
        cumulative_frequencies.append(running_total)

    total_frequency = sum(frequencies)

    print("\nCumulative Frequency Table :")
    print("{:<20}{:<15}{:<20}".format(
        "Class Interval", "Frequency", "Cumulative Frequency"
    ))
    print("-" * 55)

    for i in range(n):
        print("{:<20}{:<15}{:<20}".format(
            class_intervals[i],
            frequencies[i],
            cumulative_frequencies[i]
        ))

    print("-" * 55)
    print("Total Frequency:", total_frequency)
    print("Final Cumulative Frequency:", cumulative_frequencies[-1])

    print("\nRelative Cumulative Frequency :")

    if total_frequency > 0:
        for i in range(n):
            relative_frequency = (
                cumulative_frequencies[i] / total_frequency
            )
            percentage = relative_frequency * 100

            print(
                class_intervals[i],
                "| Cumulative Frequency:",
                cumulative_frequencies[i],
                "| Percentage:",
                round(percentage, 2), "%"
            )
    else:
        print("Relative cumulative frequencies cannot be calculated.")

    print("\nVerification :")

    if cumulative_frequencies[-1] == total_frequency:
        print("Verification successful: Final cumulative frequency equals total frequency.")
    else:
        print("Verification failed: Please check the frequency values.")

    print("\nFrequency Analysis :")
    largest_index = frequencies.index(max(frequencies))
    print("Highest Frequency Class:", class_intervals[largest_index])
    print("Highest Frequency:", frequencies[largest_index])

    print("Number of Classes:", n)

cumulativefrequencycalc()