def subsetcounter():
    print("Subset Counter :")

    n = int(input("Enter the number of elements in the set: "))

    if n < 0:
        print("Number of elements cannot be negative.")
        return

    elements = []

    for i in range(n):
        value = input("Enter element " + str(i + 1) + ": ")

        if value not in elements:
            elements.append(value)

    total_elements = len(elements)
    total_subsets = 2 ** total_elements
    proper_subsets = total_subsets - 1
    non_empty_subsets = total_subsets - 1

    print("\nSubset Count Results :")
    print("Original Set:", elements)
    print("Number of Distinct Elements:", total_elements)
    print("Total Number of Subsets:", total_subsets)
    print("Number of Proper Subsets:", proper_subsets)
    print("Number of Non-Empty Subsets:", non_empty_subsets)

    print("\nSubset Analysis :")

    if total_elements == 0:
        print("The empty set has exactly one subset: the empty set.")
    elif total_elements == 1:
        print("The set has one empty subset and one non-empty subset.")
    else:
        print("Each element can either be included or excluded.")
        print("Therefore, the total number of subsets is 2^n.")

    if total_elements <= 15:
        print("\nAll Subsets :")

        for mask in range(total_subsets):
            subset = []

            for i in range(total_elements):
                if mask & (1 << i):
                    subset.append(elements[i])

            print(subset)
    else:
        print("\nToo many subsets to display individually.")
        print("Only the subset counts are shown.")

subsetcounter()