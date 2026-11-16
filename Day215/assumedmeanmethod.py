def assumedmeanmethod():
    print("Assumed Mean Method :")

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

        if lower > upper or frequency < 0:
            print("Invalid class interval or frequency.")
            return

        class_mark = (lower + upper) / 2
        data.append((class_mark, frequency))
        total_frequency += frequency

    if total_frequency == 0:
        print("Total frequency cannot be zero.")
        return

    assumed_mean = data[0][0]
    total_fd = 0

    print("\nAssumed Mean:", assumed_mean)
    print("\nClass Mark and Deviation Table:")
    print(f"{'Class Mark':<15}{'Frequency':<15}{'d = x - A':<15}{'f × d':<15}")

    for class_mark, frequency in data:
        deviation = class_mark - assumed_mean
        fd = frequency * deviation
        total_fd += fd

        print(f"{class_mark:<15g}{frequency:<15}{deviation:<15g}{fd:<15g}")

    mean = assumed_mean + (total_fd / total_frequency)

    print("\nAssumed Mean Method Result:")
    print("Total Frequency:", total_frequency)
    print("Sum of f × d:", total_fd)
    print(f"Mean: {mean:.2f}")

assumedmeanmethod()