def datarangecalc():
    numbers = list(map(float, input("Enter data values separated by spaces: ").split()))

    if not numbers:
        print("Please enter at least one value.")
        return

    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum

    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Data Range:", data_range)

datarangecalc()