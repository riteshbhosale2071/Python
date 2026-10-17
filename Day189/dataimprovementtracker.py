def dataimprovementtracker():
    print("Data Improvement Tracker :")

    n = int(input("Enter the number of observations in each dataset: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    previous_data = []
    current_data = []

    print("\nEnter Previous Dataset Values:")

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        previous_data.append(value)

    print("\nEnter Current Dataset Values:")

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        current_data.append(value)

    previous_total = sum(previous_data)
    current_total = sum(current_data)

    previous_mean = previous_total / n
    current_mean = current_total / n

    previous_min = min(previous_data)
    previous_max = max(previous_data)

    current_min = min(current_data)
    current_max = max(current_data)

    total_change = current_total - previous_total
    mean_change = current_mean - previous_mean

    print("\nDataset Comparison :")
    print("Previous Dataset:", previous_data)
    print("Current Dataset:", current_data)

    print("\nPrevious Total:", round(previous_total, 2))
    print("Current Total:", round(current_total, 2))
    print("Total Change:", round(total_change, 2))

    print("\nPrevious Mean:", round(previous_mean, 2))
    print("Current Mean:", round(current_mean, 2))
    print("Mean Change:", round(mean_change, 2))

    print("\nIndividual Observation Changes :")

    improved = 0
    declined = 0
    unchanged = 0

    for i in range(n):
        change = current_data[i] - previous_data[i]

        print(
            "Observation", i + 1,
            "| Previous:", previous_data[i],
            "| Current:", current_data[i],
            "| Change:", round(change, 2)
        )

        if change > 0:
            improved += 1
        elif change < 0:
            declined += 1
        else:
            unchanged += 1

    print("\nImprovement Summary :")
    print("Observations Increased:", improved)
    print("Observations Decreased:", declined)
    print("Observations Unchanged:", unchanged)

    print("\nPrevious Range:", round(previous_max - previous_min, 2))
    print("Current Range:", round(current_max - current_min, 2))

    if current_mean > previous_mean:
        print("Result: The dataset mean increased.")
    elif current_mean < previous_mean:
        print("Result: The dataset mean decreased.")
    else:
        print("Result: The dataset mean remained unchanged.")

    if improved > declined:
        print("Overall Trend: More observations increased than decreased.")
    elif declined > improved:
        print("Overall Trend: More observations decreased than increased.")
    else:
        print("Overall Trend: Increases and decreases are balanced.")

    if previous_total != 0:
        percentage_change = (total_change / abs(previous_total)) * 100
        print("Total Percentage Change:", round(percentage_change, 2), "%")
    else:
        print("Total Percentage Change cannot be calculated because the previous total is zero.")

dataimprovementtracker()