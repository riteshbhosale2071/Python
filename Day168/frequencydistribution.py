def frequencydistribution():
    print("Frequency Distribution Generator :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    values.sort()

    unique_values = []
    frequencies = []

    for value in values:
        if value in unique_values:
            index = unique_values.index(value)
            frequencies[index] += 1
        else:
            unique_values.append(value)
            frequencies.append(1)

    cumulative_frequency = 0

    print("\nFrequency Distribution Table :")
    print("Value\tFrequency\tCumulative Frequency")

    for i in range(len(unique_values)):
        cumulative_frequency += frequencies[i]

        print(
            str(unique_values[i]) + "\t" +
            str(frequencies[i]) + "\t\t" +
            str(cumulative_frequency)
        )

    print("\nTotal Values:", number_of_values)
    print("Unique Values:", len(unique_values))
    print("Total Frequency:", cumulative_frequency)

frequencydistribution()