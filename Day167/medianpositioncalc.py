def medianpositioncalc():
    print("Median Position Calculator :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    values.sort()

    print("\nSorted Values:", values)

    if number_of_values % 2 == 1:
        position = (number_of_values + 1) / 2
        median = values[number_of_values // 2]

        print("Median Position:", int(position))
        print("Median Value:", median)
    else:
        position1 = number_of_values / 2
        position2 = position1 + 1

        value1 = values[number_of_values // 2 - 1]
        value2 = values[number_of_values // 2]

        median = (value1 + value2) / 2

        print("First Median Position:", int(position1))
        print("Second Median Position:", int(position2))
        print("First Median Value:", value1)
        print("Second Median Value:", value2)
        print("Median:", round(median, 2))

medianpositioncalc()