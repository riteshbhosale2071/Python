def cumulativefrequency():
    print("Cumulative Frequency Calculator")

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

    cumulative_frequency = 0

    print("\nCumulative Frequency Table:")
    print(f"{'Class Interval':<20}{'Frequency':<15}{'Cumulative Frequency':<25}")

    for lower, upper, frequency in data:
        cumulative_frequency += frequency
        print(f"{lower:g} - {upper:g}{'':<10}{frequency:<15}{cumulative_frequency:<25}")

    print("\nTotal Frequency:", cumulative_frequency)

cumulativefrequency()