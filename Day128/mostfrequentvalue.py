def mostfrequentvalue():
    data = input("Enter values separated by spaces: ").split()

    if not data:
        print("Please enter at least one value.")
        return

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    maximum_frequency = max(frequency.values())
    most_frequent = [
        value for value, count in frequency.items()
        if count == maximum_frequency
    ]

    print("Most Frequent Value(s):", most_frequent)
    print("Frequency:", maximum_frequency)

mostfrequentvalue()