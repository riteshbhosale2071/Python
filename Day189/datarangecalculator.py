def datarangecalculator():
    print("Data Range Calculator :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    numbers = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        numbers.append(value)

    minimum_value = min(numbers)
    maximum_value = max(numbers)
    data_range = maximum_value - minimum_value

    sorted_numbers = sorted(numbers)

    print("\nData Range Results :")
    print("Original Dataset:", numbers)
    print("Sorted Dataset:", sorted_numbers)
    print("Minimum Value:", minimum_value)
    print("Maximum Value:", maximum_value)
    print("Data Range:", data_range)
    print("Total Observations:", n)
    print("Distinct Values:", len(set(numbers)))

    print("\nRange Analysis :")

    if data_range == 0:
        print("Result: All observations have the same value.")
    elif data_range > 0:
        print("Result: The dataset contains variation.")
    else:
        print("Result: Invalid range calculated.")

    print("Smallest Observation:", sorted_numbers[0])
    print("Largest Observation:", sorted_numbers[-1])

datarangecalculator()