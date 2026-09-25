def reallifestatistics():
    print("Real-Life Statistics Report :")

    number_of_values = int(input("Enter the number of data values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    total = 0

    for value in values:
        total += value

    mean = total / number_of_values

    sorted_values = values[:]
    sorted_values.sort()

    if number_of_values % 2 == 1:
        median = sorted_values[number_of_values // 2]
    else:
        middle1 = sorted_values[number_of_values // 2 - 1]
        middle2 = sorted_values[number_of_values // 2]
        median = (middle1 + middle2) / 2

    minimum = min(values)
    maximum = max(values)
    data_range = maximum - minimum

    variance = 0

    for value in values:
        variance += (value - mean) ** 2

    variance = variance / number_of_values

    standard_deviation = variance ** 0.5

    increasing_count = 0
    decreasing_count = 0

    for i in range(1, number_of_values):
        if values[i] > values[i - 1]:
            increasing_count += 1
        elif values[i] < values[i - 1]:
            decreasing_count += 1

    print("\nReal-Life Statistics Report :")
    print("Dataset:", values)
    print("Number of Observations:", number_of_values)
    print("Total:", round(total, 2))
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Range:", round(data_range, 2))
    print("Variance:", round(variance, 2))
    print("Standard Deviation:", round(standard_deviation, 2))

    print("\nTrend Analysis :")
    print("Increasing Changes:", increasing_count)
    print("Decreasing Changes:", decreasing_count)

    if increasing_count > decreasing_count:
        print("Overall Trend: Increasing")
    elif decreasing_count > increasing_count:
        print("Overall Trend: Decreasing")
    else:
        print("Overall Trend: Mixed or Balanced")

    print("\nStatistical Interpretation :")

    if mean > median:
        print("The mean is greater than the median.")
        print("The dataset may have a positive skew.")
    elif mean < median:
        print("The mean is less than the median.")
        print("The dataset may have a negative skew.")
    else:
        print("The mean and median are equal.")
        print("The dataset may be approximately symmetric.")

    if standard_deviation < mean * 0.1:
        print("Variability: Low")
    elif standard_deviation < mean * 0.3:
        print("Variability: Moderate")
    else:
        print("Variability: High")

    print("\nReport Generation Completed Successfully.")

reallifestatistics()