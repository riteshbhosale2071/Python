def statisticalmeasurescomparison():
    print("Statistical Measures Comparison :")

    n = int(input("Enter the number of data values: "))

    if n <= 0:
        print("Please enter a positive number of values.")
        return

    data = []

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))
        data.append(value)

    data.sort()

    mean = sum(data) / n

    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    max_frequency = max(frequency.values())

    if max_frequency == 1:
        mode = "No Mode"
    else:
        mode = [value for value, count in frequency.items() if count == max_frequency]

    data_range = max(data) - min(data)

    variance = sum((value - mean) ** 2 for value in data) / n
    standard_deviation = variance ** 0.5

    print("\nStatistical Measures Comparison:")
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Mode:", mode)
    print("Range:", round(data_range, 2))
    print("Variance:", round(variance, 2))
    print("Standard Deviation:", round(standard_deviation, 2))

    print("\nComparison:")
    print("Mean vs Median:", round(mean, 2), "vs", round(median, 2))

    if mean > median:
        print("Mean is greater than Median.")
    elif mean < median:
        print("Mean is less than Median.")
    else:
        print("Mean and Median are equal.")

    print("Minimum Value:", min(data))
    print("Maximum Value:", max(data))

statisticalmeasurescomparison()