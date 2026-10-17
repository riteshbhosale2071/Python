def completedatasetanalyzer():
    print("Complete Dataset Analyzer :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    data = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        data.append(value)

    sorted_data = sorted(data)
    total = sum(data)
    mean = total / n
    minimum = min(data)
    maximum = max(data)
    data_range = maximum - minimum

    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    frequencies = {}

    for value in data:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    highest_frequency = max(frequencies.values())
    modes = []

    for value in frequencies:
        if frequencies[value] == highest_frequency:
            modes.append(value)

    squared_deviations = 0

    for value in data:
        squared_deviations += (value - mean) ** 2

    variance = squared_deviations / n
    standard_deviation = variance ** 0.5

    print("\nDataset Overview :")
    print("Original Dataset:", data)
    print("Sorted Dataset:", sorted_data)
    print("Number of Observations:", n)
    print("Distinct Values:", len(frequencies))
    print("Total Sum:", round(total, 2))

    print("\nCentral Tendency :")
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Mode(s):", sorted(modes))
    print("Maximum Frequency:", highest_frequency)

    if len(modes) == len(frequencies):
        print("Mode Analysis: All distinct values occur equally often.")
    elif len(modes) == 1:
        print("Mode Analysis: The dataset has one mode.")
    else:
        print("Mode Analysis: The dataset has multiple modes.")

    print("\nSpread Analysis :")
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Range:", round(data_range, 2))
    print("Population Variance:", round(variance, 2))
    print("Population Standard Deviation:", round(standard_deviation, 2))

    print("\nFrequency Table :")
    print("{:<15} {:<15} {:<20}".format(
        "Value", "Frequency", "Percentage"
    ))
    print("-" * 50)

    for value in sorted(frequencies):
        frequency = frequencies[value]
        percentage = (frequency / n) * 100

        print("{:<15} {:<15} {:<20}".format(
            value, frequency, round(percentage, 2)
        ))

    print("\nQuartile Analysis :")

    lower_half = sorted_data[:n // 2]
    upper_half = sorted_data[(n + 1) // 2:]

    if len(lower_half) > 0:
        lower_size = len(lower_half)

        if lower_size % 2 == 1:
            q1 = lower_half[lower_size // 2]
        else:
            q1 = (
                lower_half[lower_size // 2 - 1] +
                lower_half[lower_size // 2]
            ) / 2

        print("First Quartile (Q1):", round(q1, 2))
    else:
        q1 = None
        print("First Quartile (Q1): Not available")

    if len(upper_half) > 0:
        upper_size = len(upper_half)

        if upper_size % 2 == 1:
            q3 = upper_half[upper_size // 2]
        else:
            q3 = (
                upper_half[upper_size // 2 - 1] +
                upper_half[upper_size // 2]
            ) / 2

        print("Third Quartile (Q3):", round(q3, 2))
    else:
        q3 = None
        print("Third Quartile (Q3): Not available")

    if q1 is not None and q3 is not None:
        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        potential_outliers = []

        for value in data:
            if value < lower_limit or value > upper_limit:
                potential_outliers.append(value)

        print("Interquartile Range (IQR):", round(iqr, 2))
        print("Lower Outlier Limit:", round(lower_limit, 2))
        print("Upper Outlier Limit:", round(upper_limit, 2))
        print("Potential Outliers:", potential_outliers)

    print("\nDataset Evaluation :")

    if mean > median:
        print("The mean is greater than the median.")
    elif mean < median:
        print("The mean is less than the median.")
    else:
        print("The mean and median are equal.")

    if standard_deviation == 0:
        print("All observations have the same value.")
    elif standard_deviation < abs(mean) * 0.1:
        print("The dataset has relatively low variation compared with its mean.")
    else:
        print("The dataset shows variation in its observations.")

    print("\nDataset analysis completed successfully.")

completedatasetanalyzer()