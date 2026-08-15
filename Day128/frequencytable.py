def frequencytable():
    data = input("Enter values separated by spaces: ").split()

    if not data:
        print("Please enter at least one value.")
        return

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    print("\nFrequency Table:")
    print("Value\tFrequency")

    for value in sorted(frequency):
        print(f"{value}\t{frequency[value]}")

frequencytable()