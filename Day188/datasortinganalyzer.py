def datasortinganalyzer():
    print("Data Sorting Analyzer :")

    number = int(input("Enter the number of elements: "))

    if number <= 0:
        print("Number of elements must be greater than zero.")
        return

    data = []

    for i in range(number):
        value = float(input("Enter element " + str(i + 1) + ": "))
        data.append(value)

    ascending = sorted(data)
    descending = sorted(data, reverse=True)

    print("\nSorting Results :")
    print("Original Data:", data)
    print("Ascending Order:", ascending)
    print("Descending Order:", descending)

    print("\nData Analysis :")
    print("Total Elements:", len(data))
    print("Smallest Value:", min(data))
    print("Largest Value:", max(data))
    print("Range:", max(data) - min(data))
    print("Sum:", round(sum(data), 2))
    print("Average:", round(sum(data) / len(data), 2))

    unique_values = sorted(set(data))
    print("Unique Values:", unique_values)
    print("Number of Unique Values:", len(unique_values))

    duplicates = []

    for value in data:
        if data.count(value) > 1 and value not in duplicates:
            duplicates.append(value)

    if duplicates:
        print("Duplicate Values:", sorted(duplicates))
    else:
        print("Duplicate Values: None")

    middle = len(ascending) // 2

    if len(ascending) % 2 == 0:
        median = (ascending[middle - 1] + ascending[middle]) / 2
    else:
        median = ascending[middle]

    print("Median:", round(median, 2))

datasortinganalyzer()