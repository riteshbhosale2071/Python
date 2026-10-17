def datasetbalanceanalyzer():
    print("Dataset Balance Analyzer :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    numbers = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        numbers.append(value)

    total = sum(numbers)
    mean = total / n
    minimum_value = min(numbers)
    maximum_value = max(numbers)
    data_range = maximum_value - minimum_value

    positive_count = 0
    negative_count = 0
    zero_count = 0

    for value in numbers:
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
        else:
            zero_count += 1

    positive_percentage = (positive_count / n) * 100
    negative_percentage = (negative_count / n) * 100
    zero_percentage = (zero_count / n) * 100

    print("\nDataset Balance Results :")
    print("Dataset:", numbers)
    print("Total Observations:", n)
    print("Total Sum:", round(total, 2))
    print("Mean:", round(mean, 2))
    print("Minimum Value:", minimum_value)
    print("Maximum Value:", maximum_value)
    print("Data Range:", round(data_range, 2))

    print("\nValue Distribution :")
    print("Positive Values:", positive_count, "(",
          round(positive_percentage, 2), "%)")
    print("Negative Values:", negative_count, "(",
          round(negative_percentage, 2), "%)")
    print("Zero Values:", zero_count, "(",
          round(zero_percentage, 2), "%)")

    print("\nBalance Analysis :")

    if positive_count == negative_count:
        print("Positive and negative values are balanced in count.")
    elif positive_count > negative_count:
        print("The dataset contains more positive values.")
    else:
        print("The dataset contains more negative values.")

    if zero_count == n:
        print("All observations are zero.")
    elif mean > 0:
        print("The dataset has a positive mean.")
    elif mean < 0:
        print("The dataset has a negative mean.")
    else:
        print("The dataset has a mean of zero.")

    if data_range == 0:
        print("All observations have the same value.")
    else:
        print("The dataset contains variation.")

    print("\nPositive, negative, and zero percentages total:",
          round(positive_percentage + negative_percentage + zero_percentage, 2), "%")

datasetbalanceanalyzer()