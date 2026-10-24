def classintervalanalyzer():
    print("Class Interval Analyzer :")

    try:
        n = int(input("Enter the number of class intervals: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of class intervals must be greater than zero.")
        return

    intervals = []

    for i in range(n):
        print("\nClass Interval", i + 1)

        try:
            lower = float(input("Enter lower class limit: "))
            upper = float(input("Enter upper class limit: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if lower >= upper:
            print("Invalid interval! Upper limit must exceed lower limit.")
            return

        intervals.append((lower, upper))

    print("\nClass Interval Analysis :")

    for i, interval in enumerate(intervals, start=1):
        lower, upper = interval
        width = upper - lower
        midpoint = (lower + upper) / 2

        print("\nClass Interval", i)
        print("Lower Limit:", lower)
        print("Upper Limit:", upper)
        print("Class Width:", round(width, 4))
        print("Class Midpoint:", round(midpoint, 4))

    print("\nInterval Consistency Check :")

    sorted_intervals = sorted(intervals, key=lambda item: item[0])
    has_overlap = False
    has_gap = False
    equal_width = True

    first_width = intervals[0][1] - intervals[0][0]

    for interval in intervals:
        width = interval[1] - interval[0]

        if abs(width - first_width) > 0.000001:
            equal_width = False

    for i in range(1, n):
        previous_lower, previous_upper = sorted_intervals[i - 1]
        current_lower, current_upper = sorted_intervals[i]

        if current_lower < previous_upper:
            has_overlap = True
            print(
                "Overlap detected between intervals:",
                (previous_lower, previous_upper),
                "and",
                (current_lower, current_upper)
            )
        elif current_lower > previous_upper:
            has_gap = True
            print(
                "Gap detected between intervals:",
                (previous_lower, previous_upper),
                "and",
                (current_lower, current_upper)
            )

    if not has_overlap:
        print("No overlapping intervals detected.")

    if not has_gap:
        print("No gaps detected between consecutive intervals.")

    if equal_width:
        print("All class intervals have equal widths.")
    else:
        print("Class intervals have different widths.")

    print("\nSummary :")
    print("Total Intervals:", n)
    print("Smallest Lower Limit:", min(item[0] for item in intervals))
    print("Largest Upper Limit:", max(item[1] for item in intervals))
    print("Equal Widths:", "Yes" if equal_width else "No")
    print("Overlapping Intervals:", "Yes" if has_overlap else "No")
    print("Gaps Between Intervals:", "Yes" if has_gap else "No")

classintervalanalyzer()