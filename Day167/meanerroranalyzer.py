def meanerroranalyzer():
    print("Mean Error Analyzer :")

    number_of_values = int(input("Enter the number of values: "))

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    if number_of_values == 0:
        print("Number of values must be greater than zero.")
        return

    total = 0

    for value in values:
        total += value

    mean = total / number_of_values
    total_absolute_error = 0
    total_squared_error = 0

    print("\nError Analysis :")

    for i in range(number_of_values):
        error = values[i] - mean
        absolute_error = abs(error)
        squared_error = error * error

        total_absolute_error += absolute_error
        total_squared_error += squared_error

        print("\nValue:", values[i])
        print("Error:", round(error, 2))
        print("Absolute Error:", round(absolute_error, 2))
        print("Squared Error:", round(squared_error, 2))

    mean_absolute_error = total_absolute_error / number_of_values
    mean_squared_error = total_squared_error / number_of_values

    print("\nMean Error Summary :")
    print("Mean:", round(mean, 2))
    print("Mean Absolute Error:", round(mean_absolute_error, 2))
    print("Mean Squared Error:", round(mean_squared_error, 2))

meanerroranalyzer()