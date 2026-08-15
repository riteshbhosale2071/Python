def bardatapercentage():
    values = list(map(float, input("Enter bar values separated by spaces: ").split()))

    if not values:
        print("Please enter at least one value.")
        return

    total = sum(values)

    if total == 0:
        print("Total cannot be zero.")
        return

    print("Percentage of Each Bar:")

    for i, value in enumerate(values, start=1):
        percentage = (value / total) * 100
        print(f"Bar {i}: {percentage:.2f}%")

bardatapercentage()