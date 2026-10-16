def missingobservationfrommean():
    print("Missing Observation from Mean :")

    number = int(input("Enter the total number of observations: "))

    if number <= 0:
        print("Number of observations must be greater than zero.")
        return

    known_sum = float(input("Enter the sum of all known observations: "))
    mean = float(input("Enter the required mean: "))

    if number == 1:
        missing_value = mean
    else:
        missing_value = (mean * number) - known_sum

    print("\nCalculation Results :")
    print("Total Observations:", number)
    print("Required Mean:", round(mean, 2))
    print("Sum of Known Observations:", round(known_sum, 2))
    print("Missing Observation:", round(missing_value, 2))

    if missing_value > 0:
        print("The missing observation is positive.")
    elif missing_value < 0:
        print("The missing observation is negative.")
    else:
        print("The missing observation is zero.")

    calculated_mean = (known_sum + missing_value) / number
    print("Verified Mean:", round(calculated_mean, 2))

missingobservationfrommean()