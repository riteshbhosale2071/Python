def frequencytablebuilder():
    print("Frequency Table Builder :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    numbers = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        numbers.append(value)

    frequencies = {}

    for value in numbers:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    sorted_values = sorted(frequencies.keys())

    print("\nFrequency Table :")
    print("{:<15} {:<15} {:<20}".format("Value", "Frequency", "Cumulative Frequency"))
    print("-" * 50)

    cumulative_frequency = 0

    for value in sorted_values:
        frequency = frequencies[value]
        cumulative_frequency += frequency

        print("{:<15} {:<15} {:<20}".format(
            value, frequency, cumulative_frequency
        ))

    print("-" * 50)
    print("Total Observations:", n)
    print("Distinct Values:", len(frequencies))

    print("\nRelative Frequency :")

    for value in sorted_values:
        relative_frequency = frequencies[value] / n
        percentage = relative_frequency * 100

        print(
            str(value) + ":",
            "Relative Frequency =", round(relative_frequency, 3),
            "| Percentage =", round(percentage, 2), "%"
        )

frequencytablebuilder()