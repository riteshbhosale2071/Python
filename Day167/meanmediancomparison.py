def meanmediancomparison():
    print("Mean-Median Comparison :")

    number_of_values = int(input("Enter the number of values: "))

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

    values.sort()

    if number_of_values % 2 == 1:
        median = values[number_of_values // 2]
    else:
        middle1 = values[number_of_values // 2 - 1]
        middle2 = values[number_of_values // 2]
        median = (middle1 + middle2) / 2

    difference = mean - median

    print("\nSorted Values:", values)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Mean - Median:", round(difference, 2))

    if mean > median:
        print("Result: Mean is greater than the median.")
        print("Distribution: May be positively skewed.")
    elif mean < median:
        print("Result: Mean is less than the median.")
        print("Distribution: May be negatively skewed.")
    else:
        print("Result: Mean and median are equal.")
        print("Distribution: May be symmetric.")

meanmediancomparison()