def datasettrendanalyzer():
    print("Dataset Trend Analyzer :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    increasing_count = 0
    decreasing_count = 0
    equal_count = 0

    total_change = 0

    print("\nTrend Analysis :")

    for i in range(1, number_of_values):
        change = values[i] - values[i - 1]
        total_change += change

        if change > 0:
            increasing_count += 1
            trend = "Increasing"
        elif change < 0:
            decreasing_count += 1
            trend = "Decreasing"
        else:
            equal_count += 1
            trend = "No Change"

        print(
            "From", values[i - 1],
            "to", values[i],
            "Change:", round(change, 2),
            "Trend:", trend
        )

    print("\nTrend Summary :")
    print("Dataset:", values)
    print("Increasing Changes:", increasing_count)
    print("Decreasing Changes:", decreasing_count)
    print("Equal Changes:", equal_count)
    print("Total Change:", round(total_change, 2))

    if increasing_count > decreasing_count:
        print("Overall Trend: Increasing")
    elif decreasing_count > increasing_count:
        print("Overall Trend: Decreasing")
    else:
        print("Overall Trend: Mixed or Balanced")

    if total_change > 0:
        print("Final Result: The dataset increased overall.")
    elif total_change < 0:
        print("Final Result: The dataset decreased overall.")
    else:
        print("Final Result: The dataset has no overall change.")

datasettrendanalyzer()