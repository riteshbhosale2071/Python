def uniqueelementextractor():
    print("Unique Element Extractor :")

    n = int(input("Enter the number of elements: "))

    if n <= 0:
        print("Number of elements must be greater than zero.")
        return

    elements = []

    for i in range(n):
        value = input("Enter element " + str(i + 1) + ": ")
        elements.append(value)

    unique_elements = []

    for value in elements:
        if value not in unique_elements:
            unique_elements.append(value)

    frequency = {}

    for value in elements:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    single_occurrence = []

    for value in unique_elements:
        if frequency[value] == 1:
            single_occurrence.append(value)

    print("\nExtraction Results :")
    print("Original Dataset:", elements)
    print("Unique Elements:", unique_elements)
    print("Total Elements:", len(elements))
    print("Distinct Elements:", len(unique_elements))
    print("Duplicate Elements:", len(elements) - len(unique_elements))
    print("Elements Appearing Once:", single_occurrence)

    print("\nFrequency Analysis :")

    for value in unique_elements:
        print(value, "appears", frequency[value], "time(s)")

    print("\nSummary :")

    if len(unique_elements) == len(elements):
        print("All elements are unique.")
    elif len(single_occurrence) == 0:
        print("Every distinct element appears more than once.")
    else:
        print("The dataset contains both unique and repeated elements.")

uniqueelementextractor()