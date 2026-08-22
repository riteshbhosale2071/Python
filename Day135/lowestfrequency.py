def lowestfrequency():
    numbers = input("Enter values separated by spaces: ").split()

    if not numbers:
        print("Please enter at least one value.")
        return

    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    lowest_frequency = min(frequency.values())

    least_frequent = [
        value for value, count in frequency.items()
        if count == lowest_frequency
    ]

    print("Lowest Frequency:", lowest_frequency)
    print("Least Frequent Value(s):", least_frequent)

lowestfrequency()