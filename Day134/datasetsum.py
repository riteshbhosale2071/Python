def datasetsum():
    numbers = list(map(float, input("Enter dataset values separated by spaces: ").split()))

    if not numbers:
        print("Please enter at least one value.")
        return

    total = sum(numbers)

    print("Dataset Sum:", total)

datasetsum()