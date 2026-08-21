def frequencycounter():
    numbers = input("Enter values separated by spaces: ").split()

    if not numbers:
        print("Please enter at least one value.")
        return

    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    print("Frequency Count:")
    for value, count in frequency.items():
        print(value, ":", count)

frequencycounter()