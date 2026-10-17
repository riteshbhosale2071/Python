def mostcommonvalue():
    print("Most Common Value :")

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

    highest_frequency = max(frequencies.values())
    common_values = []

    for value in frequencies:
        if frequencies[value] == highest_frequency:
            common_values.append(value)

    print("\nOriginal Dataset:", numbers)
    print("\nFrequency Analysis :")

    for value in sorted(frequencies):
        print("Value:", value, "| Frequency:", frequencies[value])

    print("\nMost Common Value(s):", sorted(common_values))
    print("Highest Frequency:", highest_frequency)

    if len(common_values) == len(frequencies):
        print("Result: All distinct values occur equally often.")
    elif len(common_values) == 1:
        print("Result: The dataset has one most common value.")
    else:
        print("Result: The dataset has multiple equally common values.")

    print("Total Observations:", n)
    print("Distinct Values:", len(frequencies))

mostcommonvalue()