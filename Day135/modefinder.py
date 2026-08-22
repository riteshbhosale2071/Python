def modefinder():
    numbers = input("Enter values separated by spaces: ").split()

    if not numbers:
        print("Please enter at least one value.")
        return

    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    highest_frequency = max(frequency.values())

    modes = [
        value for value, count in frequency.items()
        if count == highest_frequency
    ]

    print("Mode:", modes)
    print("Frequency:", highest_frequency)

modefinder()