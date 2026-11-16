def groupeddatameancalculator():
    print("Grouped Data Mean Calculator")

    n = int(input("Enter the number of class intervals: "))

    if n <= 0:
        print("Please enter a positive number of intervals.")
        return

    total_fx = 0
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
        fx = frequency * class_mark

        total_fx += fx
        total_frequency += frequency

        print(f"Class Mark: {class_mark:g}")
        print(f"f × x: {fx:g}")

    if total_frequency == 0:
        print("Total frequency cannot be zero.")
        return

    mean = total_fx / total_frequency

    print("\nGrouped Data Mean Result:")
    print("Total Frequency:", total_frequency)
    print("Sum of f × x:", total_fx)
    print(f"Mean: {mean:.2f}")

groupeddatameancalculator()