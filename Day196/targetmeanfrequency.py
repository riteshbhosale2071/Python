def targetmeanfrequency():
    print("Target Mean Frequency :")

    try:
        n = int(input("Enter the number of class intervals: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of class intervals must be greater than zero.")
        return

    intervals = []
    frequencies = []
    missing_index = -1

    for i in range(n):
        print("\nClass Interval", i + 1)

        try:
            lower = float(input("Enter lower class limit: "))
            upper = float(input("Enter upper class limit: "))
        except ValueError:
            print("Invalid class limits!")
            return

        if lower >= upper:
            print("Upper limit must be greater than lower limit.")
            return

        frequency_input = input(
            "Enter frequency (or type 'missing'): "
        ).strip().lower()

        if frequency_input == "missing":
            if missing_index != -1:
                print("Only one frequency can be missing.")
                return

            missing_index = i
            frequency = None
        else:
            try:
                frequency = int(frequency_input)
            except ValueError:
                print("Frequency must be a non-negative integer or 'missing'.")
                return

            if frequency < 0:
                print("Frequency cannot be negative.")
                return

        intervals.append((lower, upper))
        frequencies.append(frequency)

    if missing_index == -1:
        print("No missing frequency was entered.")
        return

    try:
        target_mean = float(input("\nEnter the target arithmetic mean: "))
    except ValueError:
        print("Invalid target mean!")
        return

    known_frequency = 0
    known_product = 0

    for i in range(n):
        if frequencies[i] is not None:
            midpoint = (intervals[i][0] + intervals[i][1]) / 2
            known_frequency += frequencies[i]
            known_product += midpoint * frequencies[i]

    missing_midpoint = (
        intervals[missing_index][0] + intervals[missing_index][1]
    ) / 2

    denominator = missing_midpoint - target_mean

    print("\nCalculation :")
    print("Target Mean:", target_mean)
    print("Known Total Frequency:", known_frequency)
    print("Known Sum of Frequency × Midpoint:", round(known_product, 4))
    print("Missing Class Midpoint:", missing_midpoint)

    if abs(denominator) < 0.000001:
        if abs(known_product - target_mean * known_frequency) < 0.000001:
            print("\nThe target mean equation has infinitely many possible frequencies.")
            print("A unique missing frequency cannot be determined.")
        else:
            print("\nNo solution exists for the given target mean.")
        return

    missing_frequency = (
        target_mean * known_frequency - known_product
    ) / denominator

    print("\nCalculated Missing Frequency:", round(missing_frequency, 4))

    if missing_frequency < 0:
        print("No valid solution: Frequency cannot be negative.")
        return

    if abs(missing_frequency - round(missing_frequency)) > 0.000001:
        print("The result is not a whole number.")
        print("A valid frequency cannot be assigned.")
        return

    missing_frequency = int(round(missing_frequency))
    frequencies[missing_index] = missing_frequency

    total_frequency = sum(frequencies)
    total_product = 0

    print("\nCompleted Frequency Table :")
    print("{:<20}{:<15}{:<15}{:<15}".format(
        "Class Interval", "Frequency", "Midpoint", "f × Midpoint"
    ))
    print("-" * 65)

    for i in range(n):
        lower, upper = intervals[i]
        midpoint = (lower + upper) / 2
        product = frequencies[i] * midpoint
        total_product += product

        interval = str(lower) + "-" + str(upper)

        print("{:<20}{:<15}{:<15.2f}{:<15.2f}".format(
            interval, frequencies[i], midpoint, product
        ))

    print("-" * 65)
    print("Total Frequency:", total_frequency)
    print("Total Frequency × Midpoint:", round(total_product, 4))

    if total_frequency > 0:
        calculated_mean = total_product / total_frequency

        print("\nVerification :")
        print("Target Mean:", target_mean)
        print("Calculated Mean:", round(calculated_mean, 4))

        if abs(calculated_mean - target_mean) < 0.000001:
            print("Verification successful: The target mean is satisfied.")
        else:
            print("Verification failed: The target mean does not match.")
    else:
        print("Mean cannot be calculated because total frequency is zero.")

    print("\nMissing Frequency:", missing_frequency)

targetmeanfrequency()