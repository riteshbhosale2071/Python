def stepdeviationmethodcalculator():
    print("Step Deviation Method Calculator")

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
    class_width = data[0][0] - data[1][0] if n > 1 else 1

    if class_width == 0:
        print("Class width cannot be zero.")
        return

    total_fu = 0

    print("\nAssumed Mean:", assumed_mean)
    print("Class Width:", abs(class_width))
    print("\nStep Deviation Table:")
    print(f"{'Class Mark':<15}{'Frequency':<15}{'u':<15}{'f × u':<15}")

    for class_mark, frequency in data:
        u = (class_mark - assumed_mean) / abs(class_width)
        fu = frequency * u
        total_fu += fu

        print(f"{class_mark:<15g}{frequency:<15}{u:<15g}{fu:<15g}")

    mean = assumed_mean + (total_fu / total_frequency) * abs(class_width)

    print("\nStep Deviation Method Result:")
    print("Total Frequency:", total_frequency)
    print("Sum of f × u:", total_fu)
    print(f"Mean: {mean:.2f}")

stepdeviationmethodcalculator()