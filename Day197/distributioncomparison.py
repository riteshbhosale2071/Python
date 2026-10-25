def distributioncomparison():
    print("Distribution Comparison :")

    try:
        n1 = int(input("Enter the number of values in Distribution 1: "))
        if n1 <= 0:
            print("Number of values must be greater than zero.")
            return

        distribution1 = []

        for i in range(n1):
            value = float(input("Enter value " + str(i + 1) + " for Distribution 1: "))
            distribution1.append(value)

        n2 = int(input("\nEnter the number of values in Distribution 2: "))
        if n2 <= 0:
            print("Number of values must be greater than zero.")
            return

        distribution2 = []

        for i in range(n2):
            value = float(input("Enter value " + str(i + 1) + " for Distribution 2: "))
            distribution2.append(value)

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    def calculate_mean(data):
        return sum(data) / len(data)

    def calculate_variance(data):
        mean = calculate_mean(data)
        total = 0

        for value in data:
            total += (value - mean) ** 2

        return total / len(data)

    def calculate_median(data):
        sorted_data = sorted(data)
        size = len(sorted_data)

        if size % 2 == 1:
            return sorted_data[size // 2]

        return (
            sorted_data[size // 2 - 1] + sorted_data[size // 2]
        ) / 2

    def calculate_range(data):
        return max(data) - min(data)

    def calculate_standard_deviation(data):
        return calculate_variance(data) ** 0.5

    def display_distribution(name, data):
        mean = calculate_mean(data)
        median = calculate_median(data)
        variance = calculate_variance(data)
        standard_deviation = calculate_standard_deviation(data)
        data_range = calculate_range(data)

        print("\n" + name + " Statistics :")
        print("Number of Values:", len(data))
        print("Minimum:", min(data))
        print("Maximum:", max(data))
        print("Mean:", round(mean, 4))
        print("Median:", round(median, 4))
        print("Range:", round(data_range, 4))
        print("Population Variance:", round(variance, 4))
        print("Population Standard Deviation:", round(standard_deviation, 4))

        return {
            "mean": mean,
            "median": median,
            "range": data_range,
            "variance": variance,
            "standard_deviation": standard_deviation
        }

    stats1 = display_distribution("Distribution 1", distribution1)
    stats2 = display_distribution("Distribution 2", distribution2)

    print("\nDistribution Comparison :")

    print("Mean Difference:", round(abs(stats1["mean"] - stats2["mean"]), 4))
    print("Median Difference:", round(abs(stats1["median"] - stats2["median"]), 4))
    print("Range Difference:", round(abs(stats1["range"] - stats2["range"]), 4))
    print("Variance Difference:", round(abs(stats1["variance"] - stats2["variance"]), 4))
    print(
        "Standard Deviation Difference:",
        round(abs(stats1["standard_deviation"] - stats2["standard_deviation"]), 4)
    )

    if stats1["mean"] > stats2["mean"]:
        print("Distribution 1 has the higher mean.")
    elif stats2["mean"] > stats1["mean"]:
        print("Distribution 2 has the higher mean.")
    else:
        print("Both distributions have the same mean.")

    if stats1["standard_deviation"] < stats2["standard_deviation"]:
        print("Distribution 1 has less variability.")
    elif stats2["standard_deviation"] < stats1["standard_deviation"]:
        print("Distribution 2 has less variability.")
    else:
        print("Both distributions have the same variability.")

    if stats1["variance"] == stats2["variance"]:
        print("Both distributions have equal population variance.")
    else:
        print("The distributions differ in population variance.")

    print("\nFinal Summary :")
    print("Distribution 1:", distribution1)
    print("Distribution 2:", distribution2)
    print("Comparison completed successfully.")

distributioncomparison()