def datasetfrequency():
    data = input("Enter dataset values separated by spaces: ").split()

    if not data:
        print("Please enter at least one value.")
        return

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    print("\nDataset Frequency Analysis:")
    print("Value\tFrequency\tPercentage")

    total = len(data)

    for value, count in sorted(frequency.items()):
        percentage = (count / total) * 100
        print(f"{value}\t{count}\t\t{percentage:.2f}%")

    highest = max(frequency.values())
    lowest = min(frequency.values())

    print("\nHighest Frequency:", highest)
    print("Lowest Frequency:", lowest)

datasetfrequency()