def datasetstatistics():
    numbers = list(map(float, input("Enter dataset values separated by spaces: ").split()))

    if not numbers:
        print("Please enter at least one value.")
        return

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum

    print("Count:", count)
    print("Sum:", total)
    print("Average:", average)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Range:", data_range)

datasetstatistics()