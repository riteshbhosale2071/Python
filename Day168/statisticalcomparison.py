def statisticalcomparison():
    print("Statistical Comparison Engine :")

    number_of_values1 = int(input("Enter the number of values in Dataset 1: "))

    if number_of_values1 <= 0:
        print("Number of values must be greater than zero.")
        return

    dataset1 = []

    for i in range(number_of_values1):
        value = float(input("Enter Dataset 1 value " + str(i + 1) + ": "))
        dataset1.append(value)

    number_of_values2 = int(input("\nEnter the number of values in Dataset 2: "))

    if number_of_values2 <= 0:
        print("Number of values must be greater than zero.")
        return

    dataset2 = []

    for i in range(number_of_values2):
        value = float(input("Enter Dataset 2 value " + str(i + 1) + ": "))
        dataset2.append(value)

    total1 = 0
    total2 = 0

    for value in dataset1:
        total1 += value

    for value in dataset2:
        total2 += value

    mean1 = total1 / number_of_values1
    mean2 = total2 / number_of_values2

    sorted1 = dataset1[:]
    sorted2 = dataset2[:]

    sorted1.sort()
    sorted2.sort()

    if number_of_values1 % 2 == 1:
        median1 = sorted1[number_of_values1 // 2]
    else:
        median1 = (
            sorted1[number_of_values1 // 2 - 1] +
            sorted1[number_of_values1 // 2]
        ) / 2

    if number_of_values2 % 2 == 1:
        median2 = sorted2[number_of_values2 // 2]
    else:
        median2 = (
            sorted2[number_of_values2 // 2 - 1] +
            sorted2[number_of_values2 // 2]
        ) / 2

    minimum1 = min(dataset1)
    maximum1 = max(dataset1)

    minimum2 = min(dataset2)
    maximum2 = max(dataset2)

    range1 = maximum1 - minimum1
    range2 = maximum2 - minimum2

    variance1 = 0
    variance2 = 0

    for value in dataset1:
        variance1 += (value - mean1) ** 2

    for value in dataset2:
        variance2 += (value - mean2) ** 2

    variance1 = variance1 / number_of_values1
    variance2 = variance2 / number_of_values2

    print("\nDataset Statistics :")

    print("\nDataset 1")
    print("Mean:", round(mean1, 2))
    print("Median:", round(median1, 2))
    print("Minimum:", minimum1)
    print("Maximum:", maximum1)
    print("Range:", round(range1, 2))
    print("Variance:", round(variance1, 2))

    print("\nDataset 2")
    print("Mean:", round(mean2, 2))
    print("Median:", round(median2, 2))
    print("Minimum:", minimum2)
    print("Maximum:", maximum2)
    print("Range:", round(range2, 2))
    print("Variance:", round(variance2, 2))

    print("\nStatistical Comparison :")

    if mean1 > mean2:
        print("Dataset 1 has a higher mean.")
    elif mean2 > mean1:
        print("Dataset 2 has a higher mean.")
    else:
        print("Both datasets have the same mean.")

    if median1 > median2:
        print("Dataset 1 has a higher median.")
    elif median2 > median1:
        print("Dataset 2 has a higher median.")
    else:
        print("Both datasets have the same median.")

    if range1 > range2:
        print("Dataset 1 has a greater range.")
    elif range2 > range1:
        print("Dataset 2 has a greater range.")
    else:
        print("Both datasets have the same range.")

    if variance1 > variance2:
        print("Dataset 1 has greater variance.")
    elif variance2 > variance1:
        print("Dataset 2 has greater variance.")
    else:
        print("Both datasets have the same variance.")

    if mean1 == mean2 and median1 == median2:
        print("Both datasets have matching central tendency measures.")
    else:
        print("The datasets have different central tendency measures.")

statisticalcomparison()