def datasetduplicateanalyzer():
    print("Dataset Duplicate Analyzer :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    unique_values = []
    duplicate_values = []
    duplicate_count = 0

    for value in values:
        if value in unique_values:
            if value not in duplicate_values:
                duplicate_values.append(value)
            duplicate_count += 1
        else:
            unique_values.append(value)

    print("\nDuplicate Analysis :")
    print("Original Dataset:", values)
    print("Unique Values:", unique_values)
    print("Duplicate Values:", duplicate_values)
    print("Total Values:", number_of_values)
    print("Unique Value Count:", len(unique_values))
    print("Duplicate Entry Count:", duplicate_count)

    print("\nFrequency of Duplicate Values :")

    if len(duplicate_values) == 0:
        print("No duplicate values found.")
    else:
        for value in duplicate_values:
            frequency = 0

            for item in values:
                if item == value:
                    frequency += 1

            print("Value:", value, "Frequency:", frequency)

    if duplicate_count == 0:
        print("\nResult: The dataset contains no duplicates.")
    else:
        print("\nResult: The dataset contains duplicate values.")

    cleaned_data = []

    for value in values:
        if value not in cleaned_data:
            cleaned_data.append(value)

    print("Cleaned Dataset:", cleaned_data)

datasetduplicateanalyzer()