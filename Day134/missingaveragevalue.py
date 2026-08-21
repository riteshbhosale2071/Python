def missingaveragevalue():
    numbers = list(map(float, input("Enter known values separated by spaces: ").split()))
    total_count = int(input("Enter total number of values: "))
    average = float(input("Enter the average: "))

    if total_count <= 0 or len(numbers) >= total_count:
        print("Invalid number of values.")
        return

    missing_value = (average * total_count) - sum(numbers)

    print("Missing Value:", missing_value)

missingaveragevalue()