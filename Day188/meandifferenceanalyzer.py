def meandifferenceanalyzer():
    print("Mean Difference Analyzer :")

    n1 = int(input("Enter the number of observations in Dataset 1: "))

    if n1 <= 0:
        print("Number of observations must be greater than zero.")
        return

    dataset1 = []

    for i in range(n1):
        value = float(input("Enter Dataset 1 value " + str(i + 1) + ": "))
        dataset1.append(value)

    n2 = int(input("\nEnter the number of observations in Dataset 2: "))

    if n2 <= 0:
        print("Number of observations must be greater than zero.")
        return

    dataset2 = []

    for i in range(n2):
        value = float(input("Enter Dataset 2 value " + str(i + 1) + ": "))
        dataset2.append(value)

    mean1 = sum(dataset1) / n1
    mean2 = sum(dataset2) / n2

    difference = mean1 - mean2
    absolute_difference = abs(difference)

    print("\nMean Comparison Results :")
    print("Dataset 1:", dataset1)
    print("Dataset 2:", dataset2)
    print("Mean of Dataset 1:", round(mean1, 2))
    print("Mean of Dataset 2:", round(mean2, 2))
    print("Signed Mean Difference:", round(difference, 2))
    print("Absolute Mean Difference:", round(absolute_difference, 2))

    if mean1 > mean2:
        print("Result: Dataset 1 has the higher mean.")
    elif mean2 > mean1:
        print("Result: Dataset 2 has the higher mean.")
    else:
        print("Result: Both datasets have equal means.")

    percentage_difference = (
        absolute_difference / abs(mean2) * 100
        if mean2 != 0
        else None
    )

    if percentage_difference is not None:
        print("Difference Relative to Dataset 2:", round(percentage_difference, 2), "%")
    else:
        print("Relative percentage difference cannot be calculated because Dataset 2 mean is zero.")

    print("\nAdditional Analysis :")
    print("Dataset 1 Minimum:", min(dataset1))
    print("Dataset 1 Maximum:", max(dataset1))
    print("Dataset 2 Minimum:", min(dataset2))
    print("Dataset 2 Maximum:", max(dataset2))

meandifferenceanalyzer()