def frequencyranking():
    print("Frequency Ranking :")

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

    ranked_values = sorted(
        frequencies.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\nOriginal Dataset:", numbers)
    print("\nFrequency Ranking :")
    print("{:<10} {:<15} {:<15} {:<15}".format(
        "Rank", "Value", "Frequency", "Percentage"
    ))
    print("-" * 55)

    for rank, (value, frequency) in enumerate(ranked_values, start=1):
        percentage = (frequency / n) * 100

        print("{:<10} {:<15} {:<15} {:<15}".format(
            rank, value, frequency, round(percentage, 2)
        ))

    highest_frequency = ranked_values[0][1]
    most_frequent = []

    for value, frequency in ranked_values:
        if frequency == highest_frequency:
            most_frequent.append(value)

    print("\nHighest Frequency:", highest_frequency)
    print("Most Frequent Value(s):", most_frequent)
    print("Distinct Values:", len(frequencies))
    print("Total Observations:", n)

frequencyranking()