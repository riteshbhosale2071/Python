def statisticalsummaryreporter():
    print("Statistical Summary Reporter :")

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
            value = float(input("Enter value " + str(i + 1) + ": "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        data.append(value)

    sorted_data = sorted(data)
    total = sum(data)
    mean = total / n

    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    highest_frequency = max(frequency.values())
    modes = [
        value for value, count in frequency.items()
        if count == highest_frequency
    ]

    if highest_frequency == 1:
        modes = []

    data_range = max(data) - min(data)

    squared_differences = 0

    for value in data:
        squared_differences += (value - mean) ** 2

    population_variance = squared_differences / n
    population_std_dev = population_variance ** 0.5

    sample_variance = None
    sample_std_dev = None

    if n > 1:
        sample_variance = squared_differences / (n - 1)
        sample_std_dev = sample_variance ** 0.5

    print("\n" + "=" * 45)
    print("          STATISTICAL SUMMARY REPORT")
    print("=" * 45)

    print("\n1. DATASET INFORMATION")
    print("Number of Values:", n)
    print("Original Data:", data)
    print("Sorted Data:", sorted_data)

    print("\n2. CENTRAL TENDENCY")
    print("Mean:", round(mean, 4))
    print("Median:", round(median, 4))

    if modes:
        print("Mode:", modes)
    else:
        print("Mode: No unique mode")

    print("\n3. DATA SPREAD")
    print("Minimum Value:", min(data))
    print("Maximum Value:", max(data))
    print("Range:", round(data_range, 4))
    print("Population Variance:", round(population_variance, 4))
    print("Population Standard Deviation:", round(population_std_dev, 4))

    if n > 1:
        print("Sample Variance:", round(sample_variance, 4))
        print("Sample Standard Deviation:", round(sample_std_dev, 4))
    else:
        print("Sample Variance: Not defined for one value")
        print("Sample Standard Deviation: Not defined for one value")

    print("\n4. FREQUENCY DISTRIBUTION")
    print("{:<20}{:<15}".format("Value", "Frequency"))
    print("-" * 35)

    for value in sorted(frequency):
        print("{:<20}{:<15}".format(value, frequency[value]))

    print("\n5. QUARTILES")

    if n >= 2:
        lower_half = sorted_data[:n // 2]
        upper_half = sorted_data[(n + 1) // 2:]

        def calculate_median(values):
            size = len(values)

            if size == 0:
                return None

            if size % 2 == 1:
                return values[size // 2]

            return (values[size // 2 - 1] + values[size // 2]) / 2

        q1 = calculate_median(lower_half)
        q3 = calculate_median(upper_half)

        print("First Quartile (Q1):", round(q1, 4))
        print("Second Quartile (Q2):", round(median, 4))
        print("Third Quartile (Q3):", round(q3, 4))
        print("Interquartile Range:", round(q3 - q1, 4))
    else:
        print("Quartiles require at least two values.")

    print("\n6. DATASET INTERPRETATION")

    if mean > median:
        print("The mean is greater than the median.")
        print("The data may be influenced by larger values.")
    elif mean < median:
        print("The mean is less than the median.")
        print("The data may be influenced by smaller values.")
    else:
        print("The mean and median are equal.")

    if data_range == 0:
        print("All values are identical.")
    else:
        print("The dataset contains variation.")

    print("\n7. VERIFICATION")
    print("Total Sum:", round(total, 4))
    print("Recalculated Mean:", round(sum(data) / n, 4))

    if abs(sum(data) / n - mean) < 0.000001:
        print("Verification successful.")

    print("\n" + "=" * 45)
    print("           END OF REPORT")
    print("=" * 45)

statisticalsummaryreporter()