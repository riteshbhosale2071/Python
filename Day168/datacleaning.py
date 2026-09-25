def datacleaning():
    print("Data Cleaning Program :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    data = []

    for i in range(number_of_values):
        value = input("Enter value " + str(i + 1) + ": ")

        if value.strip() == "":
            print("Missing value skipped.")
        else:
            try:
                number = float(value)

                if number not in data:
                    data.append(number)
                else:
                    print("Duplicate value removed.")

            except:
                print("Invalid value skipped.")

    if len(data) == 0:
        print("\nNo valid data available.")
        return

    data.sort()

    total = 0

    for value in data:
        total += value

    mean = total / len(data)

    print("\nCleaned Dataset :")
    print("Cleaned Data:", data)
    print("Original Data Count:", number_of_values)
    print("Cleaned Data Count:", len(data))
    print("Removed Data Count:", number_of_values - len(data))
    print("Mean of Cleaned Data:", round(mean, 2))

    print("\nData cleaning completed successfully.")

datacleaning()