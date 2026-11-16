def groupeddatamedian():
    print("Grouped Data Median Calculator")

    n = int(input("Enter the number of class intervals: "))

    if n <= 0:
        print("Please enter a positive number of intervals.")
        return

    data = []
    total_frequency = 0

    print("\nEnter class limits and frequencies:")

    for i in range(n):
        print(f"\nClass Interval {i + 1}")
        lower = float(input("Enter lower limit: "))
        upper = float(input("Enter upper limit: "))
        frequency = int(input("Enter frequency: "))

        if lower >= upper or frequency < 0:
            print("Invalid class interval or frequency.")
            return

        data.append((lower, upper, frequency))
        total_frequency += frequency

    if total_frequency == 0:
        print("Total frequency cannot be zero.")
        return

    data.sort(key=lambda x: x[0])

    cumulative_frequency = 0
    median_position = total_frequency / 2

    for lower, upper, frequency in data:
        previous_cf = cumulative_frequency
        cumulative_frequency += frequency

        if cumulative_frequency >= median_position:
            median_class_lower = lower
            median_class_frequency = frequency
            previous_cumulative_frequency = previous_cf
            class_width = upper - lower
            break

    median = median_class_lower + (
        (median_position - previous_cumulative_frequency) /
        median_class_frequency
    ) * class_width

    print("\nGrouped Data Median Result:")
    print("Total Frequency:", total_frequency)
    print("Median Position:", median_position)
    print("Median Class:", median_class_lower, "-", median_class_lower + class_width)
    print("Median:", round(median, 2))

groupeddatamedian()