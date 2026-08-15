def leastfrequentvalue():
    data = input("Enter values separated by spaces: ").split()

    if not data:
        print("Please enter at least one value.")
        return

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    minimum_frequency = min(frequency.values())
    least_frequent = [
        value for value, count in frequency.items()
        if count == minimum_frequency
    ]

    print("Least Frequent Value(s):", least_frequent)
    print("Frequency:", minimum_frequency)

leastfrequentvalue()