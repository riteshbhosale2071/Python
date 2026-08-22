def highestfrequency():
    numbers = input("Enter values separated by spaces: ").split()

    if not numbers:
        print("Please enter at least one value.")
        return

    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    highest_frequency = max(frequency.values())

    most_frequent = [
        value for value, count in frequency.items()
        if count == highest_frequency
    ]

    print("Highest Frequency:", highest_frequency)
    print("Most Frequent Value(s):", most_frequent)

highestfrequency()