def statisticaloutlierdetector():
    print("Statistical Outlier Detector :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values < 4:
        print("Enter at least 4 values for outlier detection.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    values.sort()

    if number_of_values % 2 == 0:
        middle1 = values[number_of_values // 2 - 1]
        middle2 = values[number_of_values // 2]
        median = (middle1 + middle2) / 2
    else:
        median = values[number_of_values // 2]

    lower_half = []
    upper_half = []

    middle_index = number_of_values // 2

    for i in range(middle_index):
        lower_half.append(values[i])

    if number_of_values % 2 == 0:
        start_index = middle_index
    else:
        start_index = middle_index + 1

    for i in range(start_index, number_of_values):
        upper_half.append(values[i])

    if len(lower_half) % 2 == 0:
        q1 = (lower_half[len(lower_half) // 2 - 1] + lower_half[len(lower_half) // 2]) / 2
    else:
        q1 = lower_half[len(lower_half) // 2]

    if len(upper_half) % 2 == 0:
        q3 = (upper_half[len(upper_half) // 2 - 1] + upper_half[len(upper_half) // 2]) / 2
    else:
        q3 = upper_half[len(upper_half) // 2]

    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = []

    for value in values:
        if value < lower_limit or value > upper_limit:
            outliers.append(value)

    print("\nSorted Values:", values)
    print("First Quartile (Q1):", round(q1, 2))
    print("Median:", round(median, 2))
    print("Third Quartile (Q3):", round(q3, 2))
    print("Interquartile Range:", round(iqr, 2))
    print("Lower Limit:", round(lower_limit, 2))
    print("Upper Limit:", round(upper_limit, 2))

    if len(outliers) == 0:
        print("Outliers: None")
        print("Result: No statistical outliers detected.")
    else:
        print("Outliers:", outliers)
        print("Number of Outliers:", len(outliers))
        print("Result: Statistical outliers detected.")

statisticaloutlierdetector()