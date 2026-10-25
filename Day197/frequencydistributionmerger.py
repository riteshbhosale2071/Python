def frequencydistributionmerger():
    print("Frequency Distribution Merger :")

    try:
        n1 = int(input("Enter the number of classes in Distribution 1: "))
        if n1 <= 0:
            print("Number of classes must be greater than zero.")
            return

        distribution1 = {}

        print("\nEnter Distribution 1 details:")

        for i in range(n1):
            interval = input("Enter class interval " + str(i + 1) + ": ")

            if interval in distribution1:
                print("Duplicate class interval detected.")
                return

            frequency = int(input("Enter frequency: "))

            if frequency < 0:
                print("Frequency cannot be negative.")
                return

            distribution1[interval] = frequency

        n2 = int(input("\nEnter the number of classes in Distribution 2: "))
        if n2 <= 0:
            print("Number of classes must be greater than zero.")
            return

        distribution2 = {}

        print("\nEnter Distribution 2 details:")

        for i in range(n2):
            interval = input("Enter class interval " + str(i + 1) + ": ")

            frequency = int(input("Enter frequency: "))

            if frequency < 0:
                print("Frequency cannot be negative.")
                return

            if interval in distribution2:
                print("Duplicate class interval detected.")
                return

            distribution2[interval] = frequency

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    merged_distribution = {}

    for interval, frequency in distribution1.items():
        merged_distribution[interval] = frequency

    for interval, frequency in distribution2.items():
        if interval in merged_distribution:
            merged_distribution[interval] += frequency
        else:
            merged_distribution[interval] = frequency

    print("\nDistribution 1 :")
    for interval, frequency in distribution1.items():
        print(interval, ":", frequency)

    print("\nDistribution 2 :")
    for interval, frequency in distribution2.items():
        print(interval, ":", frequency)

    print("\nMerged Frequency Distribution :")
    print("{:<25}{:<20}".format("Class Interval", "Combined Frequency"))
    print("-" * 45)

    total_frequency = 0

    for interval, frequency in merged_distribution.items():
        print("{:<25}{:<20}".format(interval, frequency))
        total_frequency += frequency

    print("-" * 45)
    print("Total Classes in Merged Distribution:", len(merged_distribution))
    print("Total Frequency in Distribution 1:", sum(distribution1.values()))
    print("Total Frequency in Distribution 2:", sum(distribution2.values()))
    print("Total Combined Frequency:", total_frequency)

    print("\nFrequency Verification :")

    expected_total = sum(distribution1.values()) + sum(distribution2.values())

    if total_frequency == expected_total:
        print("Verification successful: All frequencies are preserved.")
    else:
        print("Verification failed: Check the input distributions.")

    print("\nShared Class Intervals :")

    shared_intervals = []

    for interval in distribution1:
        if interval in distribution2:
            shared_intervals.append(interval)

    if shared_intervals:
        for interval in shared_intervals:
            print(
                interval,
                "| Distribution 1:", distribution1[interval],
                "| Distribution 2:", distribution2[interval],
                "| Combined:", merged_distribution[interval]
            )
    else:
        print("No matching class intervals were found.")

    print("\nFrequency distribution merging completed successfully.")

frequencydistributionmerger()