def classinterval():
    print("Class Interval Generator")

    n = int(input("Enter the number of data values: "))

    if n <= 0:
        print("Please enter a positive number of values.")
        return

    data = []

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))
        data.append(value)

    minimum = min(data)
    maximum = max(data)

    class_count = int(input("Enter the number of class intervals: "))

    if class_count <= 0:
        print("Number of class intervals must be positive.")
        return

    class_width = (maximum - minimum) / class_count

    if class_width == 0:
        class_width = 1

    print("\nClass Interval Table :")
    print(f"{'Class Interval':<25}{'Frequency':<15}")

    lower = minimum
    total_frequency = 0

    for i in range(class_count):
        upper = lower + class_width

        if i == class_count - 1:
            frequency = sum(1 for value in data if lower <= value <= maximum)
            print(f"{lower:g} - {maximum:g}{'':<12}{frequency}")
        else:
            frequency = sum(1 for value in data if lower <= value < upper)
            print(f"{lower:g} - {upper:g}{'':<12}{frequency}")

        total_frequency += frequency
        lower = upper

    print("Total Frequency:", total_frequency)
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Class Width:", class_width)

classinterval()