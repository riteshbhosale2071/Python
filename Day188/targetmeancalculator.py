def targetmeancalculator():
    print("Target Mean Calculator :")

    number = int(input("Enter the number of existing observations: "))

    if number <= 0:
        print("Number of observations must be greater than zero.")
        return

    data = []

    for i in range(number):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        data.append(value)

    target_mean = float(input("Enter the target mean: "))

    current_sum = sum(data)
    current_mean = current_sum / number

    print("\nCurrent Dataset :")
    print("Observations:", data)
    print("Current Sum:", round(current_sum, 2))
    print("Current Mean:", round(current_mean, 2))
    print("Target Mean:", round(target_mean, 2))

    print("\nChoose an operation:")
    print("1. Find the single value to add")
    print("2. Find the single value to replace an observation")
    print("3. Find how many additional equal values are needed")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        required_value = target_mean * (number + 1) - current_sum

        print("\nRequired New Value:", round(required_value, 2))

        updated_data = data + [required_value]
        print("New Mean:", round(sum(updated_data) / len(updated_data), 2))

    elif choice == "2":
        position = int(input("Enter observation number to replace: "))

        if position < 1 or position > number:
            print("Invalid observation number.")
            return

        old_value = data[position - 1]
        required_value = target_mean * number - (current_sum - old_value)

        print("Original Value:", old_value)
        print("Required Replacement Value:", round(required_value, 2))

        data[position - 1] = required_value
        print("Updated Dataset:", data)
        print("New Mean:", round(sum(data) / number, 2))

    elif choice == "3":
        if current_mean == target_mean:
            print("The current mean already matches the target mean.")
            return

        if current_mean > target_mean:
            print("Adding equal values cannot lower the mean to this target.")
            return

        value = float(input("Enter the value to add repeatedly: "))

        if value <= target_mean:
            print("The added value must be greater than the target mean.")
            return

        required_count = (target_mean * number - current_sum) / (value - target_mean)

        if required_count < 0 or abs(required_count - round(required_count)) > 0.000001:
            print("No whole number of these values will produce the exact target mean.")
            print("Calculated required count:", round(required_count, 4))
            return

        required_count = int(round(required_count))
        print("Number of Additional Values Needed:", required_count)
        print("Total Observations:", number + required_count)

        final_sum = current_sum + required_count * value
        print("New Mean:", round(final_sum / (number + required_count), 2))

    else:
        print("Invalid choice. Select 1, 2, or 3.")

targetmeancalculator()