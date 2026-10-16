def modechange():
    print("Mode Change :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    numbers = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        numbers.append(value)

    frequencies = {}

    for value in numbers:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    max_frequency = max(frequencies.values())
    original_modes = []

    for value in frequencies:
        if frequencies[value] == max_frequency:
            original_modes.append(value)

    print("\nOriginal Dataset:", numbers)
    print("Original Frequencies:", frequencies)
    print("Original Mode(s):", original_modes)
    print("Original Maximum Frequency:", max_frequency)

    index = int(input("\nEnter the position of the observation to change (1 to " + str(n) + "): "))

    if index < 1 or index > n:
        print("Invalid position.")
        return

    new_value = float(input("Enter the replacement value: "))

    updated_numbers = numbers.copy()
    updated_numbers[index - 1] = new_value

    updated_frequencies = {}

    for value in updated_numbers:
        if value in updated_frequencies:
            updated_frequencies[value] += 1
        else:
            updated_frequencies[value] = 1

    new_max_frequency = max(updated_frequencies.values())
    updated_modes = []

    for value in updated_frequencies:
        if updated_frequencies[value] == new_max_frequency:
            updated_modes.append(value)

    print("\nMode Change Results :")
    print("Updated Dataset:", updated_numbers)
    print("Updated Frequencies:", updated_frequencies)
    print("Updated Mode(s):", updated_modes)
    print("Updated Maximum Frequency:", new_max_frequency)

    if original_modes == updated_modes and max_frequency == new_max_frequency:
        print("Result: The mode and its maximum frequency remain unchanged.")
    elif original_modes == updated_modes:
        print("Result: The mode remains the same, but its frequency changed.")
    else:
        print("Result: The mode or set of modes changed.")

modechange()