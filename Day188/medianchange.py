def medianchange():
    print("Median Change :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    numbers = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        numbers.append(value)

    sorted_numbers = sorted(numbers)

    if n % 2 == 1:
        original_median = sorted_numbers[n // 2]
    else:
        original_median = (
            sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]
        ) / 2

    print("\nOriginal Dataset:", numbers)
    print("Sorted Dataset:", sorted_numbers)
    print("Original Median:", original_median)

    index = int(input("\nEnter the position of the observation to change (1 to " + str(n) + "): "))

    if index < 1 or index > n:
        print("Invalid position.")
        return

    new_value = float(input("Enter the replacement value: "))

    updated_numbers = numbers.copy()
    updated_numbers[index - 1] = new_value

    updated_sorted = sorted(updated_numbers)

    if n % 2 == 1:
        new_median = updated_sorted[n // 2]
    else:
        new_median = (
            updated_sorted[n // 2 - 1] + updated_sorted[n // 2]
        ) / 2

    median_change = new_median - original_median

    print("\nMedian Change Results :")
    print("Updated Dataset:", updated_numbers)
    print("Updated Sorted Dataset:", updated_sorted)
    print("Original Median:", original_median)
    print("Updated Median:", new_median)
    print("Median Change:", median_change)

    if new_median > original_median:
        print("Result: The median increased.")
    elif new_median < original_median:
        print("Result: The median decreased.")
    else:
        print("Result: The median remained unchanged.")

medianchange()