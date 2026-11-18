def statisticalreport():
    print("Statistical Report :")

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

    highest_frequency = max(frequency.values())

    if highest_frequency == 1:
        mode = "No Mode"
    else:
        mode = [value for value, count in frequency.items() if count == highest_frequency]

    data_range = max(data) - min(data)
    variance = sum((value - mean) ** 2 for value in data) / n
    standard_deviation = variance ** 0.5

    print("\nStatistical Report:")
    print("Total Data Values:", n)
    print("Sorted Data:", data)
    print("Sum:", sum(data))
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Mode:", mode)
    print("Minimum Value:", min(data))
    print("Maximum Value:", max(data))
    print("Range:", round(data_range, 2))
    print("Variance:", round(variance, 2))
    print("Standard Deviation:", round(standard_deviation, 2))

    print("\nFrequency Distribution:")
    print(f"{'Value':<15}{'Frequency':<15}{'Percentage':<15}")

    for value, count in sorted(frequency.items()):
        percentage = count / n * 100
        print(f"{value:<15g}{count:<15}{percentage:.2f}%")

    print("\nStatistical Report Generated Successfully.")

statisticalreport()