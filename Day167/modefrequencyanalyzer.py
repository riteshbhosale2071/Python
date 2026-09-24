def modefrequencyanalyzer():
    print("Mode Frequency Analyzer :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []
    frequencies = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        frequency = int(input("Enter frequency " + str(i + 1) + ": "))

        if frequency < 0:
            print("Frequency cannot be negative.")
            return

        values.append(value)
        frequencies.append(frequency)

    highest_frequency = frequencies[0]

    for frequency in frequencies:
        if frequency > highest_frequency:
            highest_frequency = frequency

    modes = []

    for i in range(number_of_values):
        if frequencies[i] == highest_frequency:
            modes.append(values[i])

    print("\nFrequency Analysis :")

    for i in range(number_of_values):
        print("Value:", values[i], "Frequency:", frequencies[i])

    print("\nHighest Frequency:", highest_frequency)

    if highest_frequency == 0:
        print("There is no mode because all frequencies are zero.")
    elif len(modes) == 1:
        print("Mode:", modes[0])
        print("The data is unimodal.")
    else:
        print("Modes:", modes)
        print("The data is multimodal.")

    print("Number of Modes:", len(modes))

modefrequencyanalyzer()