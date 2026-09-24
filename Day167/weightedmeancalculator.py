def weightedmeancalculator():
    print("Weighted Mean Calculator :")

    number_of_values = int(input("Enter the number of values: "))

    total_weighted_value = 0
    total_weight = 0

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        weight = float(input("Enter weight of value " + str(i + 1) + ": "))

        total_weighted_value += value * weight
        total_weight += weight

    if total_weight == 0:
        print("Total weight cannot be zero.")
        return

    weighted_mean = total_weighted_value / total_weight

    print("\nTotal Weighted Value:", total_weighted_value)
    print("Total Weight:", total_weight)
    print("Weighted Mean:", round(weighted_mean, 2))

weightedmeancalculator()