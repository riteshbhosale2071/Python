def disjointcollectionchecker():
    print("Disjoint Collection Checker :")

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

    print("\nDisjoint Collection Analysis :")
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Common Elements:", common_elements)
    print("Number of Common Elements:", len(common_elements))

    if len(common_elements) == 0:
        print("Result: Set A and Set B are disjoint.")
        print("The two sets have no elements in common.")
    else:
        print("Result: Set A and Set B are not disjoint.")
        print("The sets share one or more elements.")

    union = set_a.copy()

    for value in set_b:
        if value not in union:
            union.append(value)

    print("\nAdditional Analysis :")
    print("Union of Sets:", union)
    print("Total Distinct Elements:", len(union))

    if len(common_elements) > 0:
        print("Shared Elements:", common_elements)
    else:
        print("No shared elements were found.")

    if len(set_a) == 0 or len(set_b) == 0:
        print("An empty set is disjoint from every set.")

disjointcollectionchecker()