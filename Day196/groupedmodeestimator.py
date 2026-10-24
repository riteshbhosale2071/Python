def groupedmodeestimator():
    print("Grouped Mode Estimator :")

    try:
        n = int(input("Enter the number of class intervals: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n < 3:
        print("Enter at least three class intervals for reliable mode estimation.")
        return

    classes = []
    frequencies = []

    for i in range(n):
        print("\nClass Interval", i + 1)

        try:
            lower = float(input("Enter lower class limit: "))
            upper = float(input("Enter upper class limit: "))
            frequency = int(input("Enter frequency: "))
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")
            return

        if lower >= upper:
            print("Upper class limit must be greater than lower class limit.")
            return

        if frequency < 0:
            print("Frequency cannot be negative.")
            return

        if i > 0:
            previous_lower, previous_upper = classes[i - 1]

            if lower < previous_lower:
                print("Class intervals must be entered in ascending order.")
                return

            if lower < previous_upper:
                print("Class intervals must not overlap.")
                return

        classes.append((lower, upper))
        frequencies.append(frequency)

    total_frequency = sum(frequencies)

    if total_frequency == 0:
        print("Mode cannot be estimated because all frequencies are zero.")
        return

    modal_frequency = max(frequencies)
    modal_indices = [
        i for i in range(n) if frequencies[i] == modal_frequency
    ]

    print("\nGrouped Frequency Table :")
    print("{:<20}{:<15}".format("Class Interval", "Frequency"))
    print("-" * 35)

    for i in range(n):
        lower, upper = classes[i]
        interval = str(lower) + " - " + str(upper)
        print("{:<20}{:<15}".format(interval, frequencies[i]))

    print("-" * 35)
    print("Total Frequency:", total_frequency)
    print("Highest Frequency:", modal_frequency)

    if len(modal_indices) > 1:
        print("\nMultiple classes share the highest frequency.")
        print("The modal class is not unique.")

        for index in modal_indices:
            print("Candidate Modal Class:", classes[index])

        print("A single grouped mode estimate may not be appropriate.")
        return

    modal_index = modal_indices[0]

    if modal_index == 0 or modal_index == n - 1:
        print("\nThe modal class is at the boundary of the table.")
        print("A reliable mode estimate may require additional classes.")
        return

    lower_limit, upper_limit = classes[modal_index]
    class_width = upper_limit - lower_limit

    modal_frequency = frequencies[modal_index]
    previous_frequency = frequencies[modal_index - 1]
    next_frequency = frequencies[modal_index + 1]

    d1 = modal_frequency - previous_frequency
    d2 = modal_frequency - next_frequency

    print("\nModal Class Analysis :")
    print("Modal Class:", classes[modal_index])
    print("Lower Limit (L):", lower_limit)
    print("Class Width (h):", class_width)
    print("Modal Class Frequency (f1):", modal_frequency)
    print("Previous Class Frequency (f0):", previous_frequency)
    print("Next Class Frequency (f2):", next_frequency)

    denominator = d1 + d2

    if denominator == 0:
        print("Mode cannot be estimated using the grouped mode formula.")
        return

    mode = lower_limit + (d1 / denominator) * class_width

    print("\nMode Calculation :")
    print("Formula: Mode = L + ((f1 - f0) / (2f1 - f0 - f2)) * h")
    print("Estimated Mode:", round(mode, 4))

    print("\nVerification :")

    if lower_limit <= mode <= upper_limit:
        print("The estimated mode lies within the modal class.")
    else:
        print("Warning: The estimated mode lies outside the modal class.")

    print("Total Classes:", n)
    print("Total Observations:", total_frequency)
    print("\nNote: The mode is an estimate based on grouped frequency data.")

groupedmodeestimator()