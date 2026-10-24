def missingfrequency():
    print("Missing Frequency Solver :")

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

    print("\nChoose a solving method:")
    print("1. Known total frequency")
    print("2. Known arithmetic mean")
    print("3. Known median")
    print("4. Known mode")

    choice = input("Enter your choice (1-4): ").strip()

    known_frequency = sum(
        frequency for frequency in frequencies
        if frequency is not None
    )

    missing_frequency = None

    if choice == "1":
        try:
            total_frequency = int(input("Enter the total frequency: "))
        except ValueError:
            print("Invalid total frequency!")
            return

        if total_frequency < 0:
            print("Total frequency cannot be negative.")
            return

        missing_frequency = total_frequency - known_frequency

    elif choice == "2":
        try:
            target_mean = float(input("Enter the known arithmetic mean: "))
        except ValueError:
            print("Invalid mean!")
            return

        known_product = 0

        for i in range(n):
            lower, upper = intervals[i]
            midpoint = (lower + upper) / 2

            if frequencies[i] is not None:
                known_product += midpoint * frequencies[i]

        missing_midpoint = sum(intervals[missing_index]) / 2
        denominator = missing_midpoint - target_mean

        if abs(denominator) < 0.000001:
            print("The mean equation cannot determine a unique frequency.")
            return

        missing_frequency = (
            target_mean * known_frequency - known_product
        ) / denominator

    elif choice == "3":
        try:
            target_median = float(input("Enter the known median: "))
        except ValueError:
            print("Invalid median!")
            return

        lower, upper = intervals[missing_index]
        class_width = upper - lower

        if not lower <= target_median <= upper:
            print("The median must lie within the missing-frequency class.")
            return

        previous_frequency = sum(
            frequencies[i] for i in range(missing_index)
            if frequencies[i] is not None
        )

        later_frequency = sum(
            frequencies[i] for i in range(missing_index + 1, n)
            if frequencies[i] is not None
        )

        if any(
            frequencies[i] is None
            for i in range(n)
            if i != missing_index
        ):
            print("Only one missing frequency is supported.")
            return

        denominator = 2 * (upper - target_median) / class_width - 1

        if abs(denominator) < 0.000001:
            print("The median equation cannot determine a unique frequency.")
            return

        missing_frequency = (
            2 * previous_frequency - later_frequency
        ) / denominator

    elif choice == "4":
        if missing_index == 0 or missing_index == n - 1:
            print("The missing-frequency class must have a class before and after it.")
            return

        try:
            target_mode = float(input("Enter the known mode: "))
        except ValueError:
            print("Invalid mode!")
            return

        lower, upper = intervals[missing_index]
        previous_frequency = frequencies[missing_index - 1]
        next_frequency = frequencies[missing_index + 1]

        if previous_frequency is None or next_frequency is None:
            print("Adjacent frequencies must be known.")
            return

        if not lower <= target_mode <= upper:
            print("The mode must lie within the missing-frequency class.")
            return

        class_width = upper - lower

        denominator = target_mode - lower

        if abs(denominator) < 0.000001:
            print("The mode equation cannot determine a unique frequency.")
            return

        missing_frequency = (
            previous_frequency * class_width
            + next_frequency * denominator
            - next_frequency * class_width
        ) / denominator

    else:
        print("Invalid choice! Please select from 1 to 4.")
        return

    print("\nSolution :")

    if missing_frequency < 0:
        print("No valid solution: The calculated frequency is negative.")
        return

    if abs(missing_frequency - round(missing_frequency)) > 0.000001:
        print("Calculated Frequency:", round(missing_frequency, 4))
        print("The result is not a whole number, so it is not a valid frequency.")
        return

    missing_frequency = int(round(missing_frequency))
    frequencies[missing_index] = missing_frequency

    print("Missing Class Interval:", intervals[missing_index])
    print("Missing Frequency:", missing_frequency)

    print("\nCompleted Frequency Table :")
    print("{:<20}{:<15}".format("Class Interval", "Frequency"))
    print("-" * 35)

    for i in range(n):
        print(
            "{:<20}{:<15}".format(
                str(intervals[i][0]) + "-" + str(intervals[i][1]),
                frequencies[i]
            )
        )

    print("-" * 35)
    print("Total Frequency:", sum(frequencies))

    if choice == "2":
        midpoints = [
            (lower + upper) / 2
            for lower, upper in intervals
        ]
        calculated_mean = sum(
            midpoints[i] * frequencies[i]
            for i in range(n)
        ) / sum(frequencies)

        print("Verified Mean:", round(calculated_mean, 4))

    print("\nMissing frequency solved successfully.")

missingfrequency()