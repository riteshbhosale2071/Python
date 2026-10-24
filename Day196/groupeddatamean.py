def groupeddatamean():
    print("Grouped Data Mean Calculator :")

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
    midpoints = []
    frequency_products = []

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
            print("Upper class limit must be greater than lower limit.")
            return

        if frequency < 0:
            print("Frequency cannot be negative.")
            return

        midpoint = (lower + upper) / 2
        product = midpoint * frequency

        intervals.append((lower, upper))
        frequencies.append(frequency)
        midpoints.append(midpoint)
        frequency_products.append(product)

    total_frequency = sum(frequencies)
    total_product = sum(frequency_products)

    print("\nGrouped Data Mean Table :")
    print("{:<18}{:<12}{:<12}{:<15}".format(
        "Class Interval", "Frequency", "Midpoint", "f * x"
    ))
    print("-" * 57)

    for i in range(n):
        lower, upper = intervals[i]
        interval = str(round(lower, 2)) + "-" + str(round(upper, 2))

        print("{:<18}{:<12}{:<12.2f}{:<15.2f}".format(
            interval,
            frequencies[i],
            midpoints[i],
            frequency_products[i]
        ))

    print("-" * 57)
    print("Total Frequency:", total_frequency)
    print("Sum of f * x:", round(total_product, 2))

    print("\nMean Calculation :")

    if total_frequency == 0:
        print("Mean cannot be calculated because total frequency is zero.")
        return

    mean = total_product / total_frequency

    print("Formula: Mean = Sum(f * x) / Sum(f)")
    print("Mean =", round(total_product, 2), "/", total_frequency)
    print("Arithmetic Mean:", round(mean, 4))

    print("\nVerification :")

    if abs(sum(frequency_products) - total_product) < 0.000001:
        print("Verification successful: All frequency products are included.")
    else:
        print("Verification failed: Check the calculations.")

    print("\nSummary :")
    print("Number of Classes:", n)
    print("Total Observations:", total_frequency)
    print("Calculated Mean:", round(mean, 4))

groupeddatamean()