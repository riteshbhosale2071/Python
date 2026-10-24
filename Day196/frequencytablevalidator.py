def frequencytablevalidator():
    print("Frequency Table Validator :")

    try:
        n = int(input("Enter the number of classes: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of classes must be greater than zero.")
        return

    class_intervals = []
    frequencies = []

    for i in range(n):
        print("\nClass", i + 1)

        try:
            lower = float(input("Enter lower class limit: "))
            upper = float(input("Enter upper class limit: "))
            frequency = int(input("Enter frequency: "))
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")
            return

        if lower >= upper:
            print("Error: Upper limit must be greater than lower limit.")
            return

        if frequency < 0:
            print("Error: Frequency cannot be negative.")
            return

        class_intervals.append((lower, upper))
        frequencies.append(frequency)

    try:
        expected_total = int(
            input("\nEnter the expected total frequency (or -1 to skip): ")
        )
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    errors = []
    warnings = []

    for i in range(n):
        lower, upper = class_intervals[i]

        if i > 0:
            previous_lower, previous_upper = class_intervals[i - 1]

            if lower < previous_lower:
                errors.append(
                    "Class " + str(i + 1) + " is not in ascending order."
                )
            elif lower < previous_upper:
                errors.append(
                    "Class " + str(i + 1) + " overlaps the previous class."
                )
            elif lower > previous_upper:
                warnings.append(
                    "There is a gap before class " + str(i + 1) + "."
                )

    total_frequency = sum(frequencies)

    if expected_total >= 0 and total_frequency != expected_total:
        errors.append(
            "Total frequency does not match the expected total."
        )

    print("\nFrequency Table :")
    print("{:<10}{:<15}{:<15}{:<15}".format(
        "Class", "Lower Limit", "Upper Limit", "Frequency"
    ))
    print("-" * 55)

    for i in range(n):
        lower, upper = class_intervals[i]

        print("{:<10}{:<15.2f}{:<15.2f}{:<15}".format(
            i + 1, lower, upper, frequencies[i]
        ))

    print("-" * 55)
    print("Total Classes:", n)
    print("Total Frequency:", total_frequency)

    print("\nValidation Results :")

    if errors:
        print("Errors Found:", len(errors))

        for error in errors:
            print("-", error)
    else:
        print("No structural or frequency-total errors detected.")

    if warnings:
        print("\nWarnings:", len(warnings))

        for warning in warnings:
            print("-", warning)

    print("\nRelative Frequency Check :")

    if total_frequency > 0:
        relative_total = 0

        for i in range(n):
            relative_frequency = frequencies[i] / total_frequency
            relative_total += relative_frequency

            print(
                "Class", i + 1,
                "| Relative Frequency:", round(relative_frequency, 4),
                "| Percentage:", round(relative_frequency * 100, 2), "%"
            )

        print("Total Relative Frequency:", round(relative_total, 4))

        if abs(relative_total - 1) < 0.000001:
            print("Relative frequency check passed.")
        else:
            print("Relative frequency check failed.")
    else:
        print("Relative frequencies cannot be calculated because total frequency is zero.")

    if errors:
        print("\nFinal Status: Invalid frequency table.")
    elif warnings:
        print("\nFinal Status: Valid with warnings.")
    else:
        print("\nFinal Status: Frequency table passed all checks.")

frequencytablevalidator()