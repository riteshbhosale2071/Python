def meanchange():
    print("Mean Change :")

    number = int(input("Enter the number of data values: "))

    if number <= 0:
        print("Number of values must be greater than zero.")
        return

    data = []

    for i in range(number):
        value = float(input("Enter value " + str(i + 1) + ": "))
        data.append(value)

    original_mean = sum(data) / len(data)

    print("\nOriginal Dataset:", data)
    print("Original Mean:", round(original_mean, 2))

    print("\nChoose a change operation:")
    print("1. Add a new value")
    print("2. Remove an existing value")
    print("3. Increase all values")
    print("4. Decrease all values")
    print("5. Multiply all values by a factor")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        new_value = float(input("Enter the new value: "))
        data.append(new_value)

    elif choice == "2":
        value = float(input("Enter the value to remove: "))

        if value not in data:
            print("Value not found in the dataset.")
            return

        data.remove(value)

        if len(data) == 0:
            print("Cannot calculate the mean of an empty dataset.")
            return

    elif choice == "3":
        increase = float(input("Enter the amount to increase: "))
        data = [value + increase for value in data]

    elif choice == "4":
        decrease = float(input("Enter the amount to decrease: "))
        data = [value - decrease for value in data]

    elif choice == "5":
        factor = float(input("Enter the multiplication factor: "))
        data = [value * factor for value in data]

    else:
        print("Invalid choice. Select a number from 1 to 5.")
        return

    new_mean = sum(data) / len(data)
    mean_difference = new_mean - original_mean

    print("\nMean Change Results :")
    print("Updated Dataset:", data)
    print("Original Mean:", round(original_mean, 2))
    print("New Mean:", round(new_mean, 2))
    print("Mean Difference:", round(mean_difference, 2))

    if mean_difference > 0:
        print("Result: The mean increased.")
    elif mean_difference < 0:
        print("Result: The mean decreased.")
    else:
        print("Result: The mean remained unchanged.")

meanchange()