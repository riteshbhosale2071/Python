def statisticalranking():
    print("Statistical Ranking Program :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    sorted_values = values[:]
    sorted_values.sort(reverse=True)

    print("\n=== Statistical Ranking ===")
    print("Rank\tValue\tPercentile Rank")

    for i in range(number_of_values):
        value = sorted_values[i]
        rank = i + 1
        percentile_rank = ((number_of_values - rank) / number_of_values) * 100

        print(
            str(rank) + "\t" +
            str(value) + "\t" +
            str(round(percentile_rank, 2))
        )

    print("\nOriginal Values and Ranks :")

    for value in values:
        rank = 1

        for sorted_value in sorted_values:
            if sorted_value > value:
                rank += 1

        percentile_rank = ((number_of_values - rank) / number_of_values) * 100

        print(
            "Value:", value,
            "Rank:", rank,
            "Percentile Rank:", round(percentile_rank, 2)
        )

statisticalranking()