def commonelementfinder():
    print("Common Element Finder :")

    n1 = int(input("Enter the number of elements in Set A: "))

    if n1 < 0:
        print("Number of elements cannot be negative.")
        return

    set_a = []

    for i in range(n1):
        value = input("Enter element " + str(i + 1) + " of Set A: ")

        if value not in set_a:
            set_a.append(value)

    n2 = int(input("\nEnter the number of elements in Set B: "))

    if n2 < 0:
        print("Number of elements cannot be negative.")
        return

    set_b = []

    for i in range(n2):
        value = input("Enter element " + str(i + 1) + " of Set B: ")

        if value not in set_b:
            set_b.append(value)

    common_elements = []

    for value in set_a:
        if value in set_b:
            common_elements.append(value)

    only_a = []

    for value in set_a:
        if value not in set_b:
            only_a.append(value)

    only_b = []

    for value in set_b:
        if value not in set_a:
            only_b.append(value)

    print("\nCommon Element Results :")
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Common Elements:", common_elements)
    print("Number of Common Elements:", len(common_elements))

    print("\nSet Analysis :")
    print("Elements Only in Set A:", only_a)
    print("Elements Only in Set B:", only_b)

    union = set_a.copy()

    for value in set_b:
        if value not in union:
            union.append(value)

    print("Union of Sets:", union)
    print("Total Distinct Elements in Union:", len(union))

    if len(common_elements) == 0:
        print("Result: The sets have no common elements.")
    elif len(common_elements) == len(set_a) and len(common_elements) == len(set_b):
        print("Result: Both sets are equal.")
    else:
        print("Result: The sets share some common elements.")

    if len(union) > 0:
        similarity = (len(common_elements) / len(union)) * 100
        print("Jaccard Similarity:", round(similarity, 2), "%")
    else:
        print("Jaccard Similarity: Not defined for two empty sets.")

commonelementfinder()