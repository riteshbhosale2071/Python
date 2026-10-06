def mathematicaldatavalidator():
    print("Mathematical Data Validator :")

    number_of_values = int(input("Enter number of values: "))

    if number_of_values <= 0:
        print("Enter a valid number of values.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    print("\nData Validation :")

    valid = True

    for i in range(number_of_values):
        if values[i] < 0:
            print("Value", i + 1, "is negative.")
            valid = False

    duplicate_found = False

    for i in range(number_of_values):
        for j in range(i + 1, number_of_values):
            if values[i] == values[j]:
                print("Duplicate value found:", values[i])
                duplicate_found = True

    increasing = True

    for i in range(number_of_values - 1):
        if values[i] > values[i + 1]:
            increasing = False
            break

    decreasing = True

    for i in range(number_of_values - 1):
        if values[i] < values[i + 1]:
            decreasing = False
            break

    if increasing:
        print("Data is in non-decreasing order.")
    elif decreasing:
        print("Data is in non-increasing order.")
    else:
        print("Data is not ordered.")

    if duplicate_found:
        print("Validation: Duplicate values exist.")
    else:
        print("Validation: No duplicate values found.")

    if valid:
        print("Validation: All values are non-negative.")
    else:
        print("Validation: Negative values detected.")

    minimum = min(values)
    maximum = max(values)

    print("\nMinimum Value:", minimum)
    print("Maximum Value:", maximum)

mathematicaldatavalidator()