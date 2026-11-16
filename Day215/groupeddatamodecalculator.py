def groupeddatamodecalculator():
    print("Grouped Data Mode Calculator")

    n = int(input("Enter the number of class intervals: "))

    if n <= 0:
        print("Please enter a positive number of intervals.")
        return

    data = []

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

    data.sort(key=lambda x: x[0])

    modal_index = max(range(n), key=lambda i: data[i][2])

    if data[modal_index][2] == 0:
        print("All frequencies are zero. Mode cannot be calculated.")
        return

    lower_limit = data[modal_index][0]
    upper_limit = data[modal_index][1]
    modal_frequency = data[modal_index][2]

    previous_frequency = data[modal_index - 1][2] if modal_index > 0 else 0
    next_frequency = data[modal_index + 1][2] if modal_index < n - 1 else 0

    class_width = upper_limit - lower_limit

    denominator = (2 * modal_frequency) - previous_frequency - next_frequency

    if denominator == 0:
        print("Mode cannot be calculated using the grouped data formula.")
        return

    mode = lower_limit + (
        (modal_frequency - previous_frequency) / denominator
    ) * class_width

    print("\nGrouped Data Mode Result:")
    print("Modal Class:", lower_limit, "-", upper_limit)
    print("Modal Frequency:", modal_frequency)
    print("Previous Frequency:", previous_frequency)
    print("Next Frequency:", next_frequency)
    print("Mode:", round(mode, 2))

groupeddatamodecalculator()