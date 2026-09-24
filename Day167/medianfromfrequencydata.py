def medianfromfrequencydata():
    print("Median from Frequency Data :")

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

    for i in range(number_of_values):
        for j in range(i + 1, number_of_values):
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
                frequencies[i], frequencies[j] = frequencies[j], frequencies[i]

    total_frequency = 0

    for frequency in frequencies:
        total_frequency += frequency

    if total_frequency == 0:
        print("Total frequency cannot be zero.")
        return

    print("\nSorted Frequency Data:")

    for i in range(number_of_values):
        print("Value:", values[i], "Frequency:", frequencies[i])

    if total_frequency % 2 == 1:
        median_position = (total_frequency + 1) // 2
        first_position = median_position
        second_position = median_position
    else:
        first_position = total_frequency // 2
        second_position = first_position + 1

    cumulative_frequency = 0
    first_median = 0
    second_median = 0

    for i in range(number_of_values):
        cumulative_frequency += frequencies[i]

        if first_median == 0 and cumulative_frequency >= first_position:
            first_median = values[i]

        if second_median == 0 and cumulative_frequency >= second_position:
            second_median = values[i]

    median = (first_median + second_median) / 2

    print("\nTotal Frequency:", total_frequency)
    print("First Median Position:", first_position)
    print("Second Median Position:", second_position)
    print("First Median Value:", first_median)
    print("Second Median Value:", second_median)
    print("Median:", round(median, 2))

medianfromfrequencydata()