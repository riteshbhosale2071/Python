def datasetsymmetrychecker():
    print("Dataset Symmetry Checker :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    values.sort()

    total = 0

    for value in values:
        total += value

    mean = total / number_of_values

    if number_of_values % 2 == 1:
        median = values[number_of_values // 2]
    else:
        middle1 = values[number_of_values // 2 - 1]
        middle2 = values[number_of_values // 2]
        median = (middle1 + middle2) / 2

    left_deviation = 0
    right_deviation = 0

    for i in range(number_of_values // 2):
        left_deviation += abs(values[i] - median)
        right_deviation += abs(values[number_of_values - 1 - i] - median)

    difference = abs(left_deviation - right_deviation)

    print("\nSorted Dataset:", values)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Left Deviation:", round(left_deviation, 2))
    print("Right Deviation:", round(right_deviation, 2))
    print("Deviation Difference:", round(difference, 2))

    if difference < 0.000001:
        print("Result: The dataset is symmetric around the median.")
    else:
        print("Result: The dataset is not symmetric around the median.")

    if abs(mean - median) < 0.000001:
        print("Mean-Median Status: Mean and median are equal.")
    elif mean > median:
        print("Mean-Median Status: Mean is greater than median.")
    else:
        print("Mean-Median Status: Mean is less than median.")

datasetsymmetrychecker()