def datacomparisonreport():
    data1 = list(map(float, input("Enter first dataset values separated by spaces: ").split()))
    data2 = list(map(float, input("Enter second dataset values separated by spaces: ").split()))

    if not data1 or not data2:
        print("Please enter values in both datasets.")
        return

    print("\nData Comparison Report :")

    print("Dataset 1:")
    print("Count:", len(data1))
    print("Sum:", sum(data1))
    print("Average:", sum(data1) / len(data1))
    print("Maximum:", max(data1))
    print("Minimum:", min(data1))

    print("\nDataset 2:")
    print("Count:", len(data2))
    print("Sum:", sum(data2))
    print("Average:", sum(data2) / len(data2))
    print("Maximum:", max(data2))
    print("Minimum:", min(data2))

    average1 = sum(data1) / len(data1)
    average2 = sum(data2) / len(data2)

    print("\nComparison :")

    if average1 > average2:
        print("Dataset 1 has the higher average.")
    elif average1 < average2:
        print("Dataset 2 has the higher average.")
    else:
        print("Both datasets have the same average.")

    print("Average Difference:", abs(average1 - average2))
    print("Total Difference:", abs(sum(data1) - sum(data2)))

datacomparisonreport()