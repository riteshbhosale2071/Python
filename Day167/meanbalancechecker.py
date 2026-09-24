def meanbalancechecker():
    print("Mean Balance Checker :")

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
    positive_deviation = 0
    negative_deviation = 0
    total_deviation = 0

    print("\nMean Balance Analysis :")
    print("Mean:", round(mean, 2))

    for value in values:
        deviation = value - mean
        total_deviation += deviation

        if deviation > 0:
            positive_deviation += deviation
        elif deviation < 0:
            negative_deviation += deviation

        print("Value:", value, "Deviation:", round(deviation, 2))

    print("\nPositive Deviation:", round(positive_deviation, 2))
    print("Negative Deviation:", round(negative_deviation, 2))
    print("Total Deviation:", round(total_deviation, 2))

    if abs(total_deviation) < 0.000001:
        print("Result: The data is balanced around the mean.")
    else:
        print("Result: The data is not balanced around the mean.")

    if round(positive_deviation, 2) == round(abs(negative_deviation), 2):
        print("Balance Status: Positive and negative deviations are equal.")
    else:
        print("Balance Status: Positive and negative deviations are different.")

meanbalancechecker()