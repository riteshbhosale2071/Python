def subsetvalidator():
    print("Subset Validator :")

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

    is_subset = True
    missing_elements = []

    for value in set_a:
        if value not in set_b:
            is_subset = False
            missing_elements.append(value)

    print("\nSubset Validation Results :")
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Cardinality of Set A:", len(set_a))
    print("Cardinality of Set B:", len(set_b))

    if is_subset:
        print("Result: Set A is a subset of Set B.")
        print("Every element of Set A exists in Set B.")

        if len(set_a) < len(set_b):
            print("Set A is a proper subset of Set B.")
        else:
            print("Set A is equal to Set B.")
    else:
        print("Result: Set A is not a subset of Set B.")
        print("Elements missing from Set B:", missing_elements)

    is_superset = True

    for value in set_b:
        if value not in set_a:
            is_superset = False
            break

    if is_superset:
        print("Set A is also a superset of Set B.")
    else:
        print("Set A is not a superset of Set B.")

    common_elements = []

    for value in set_a:
        if value in set_b:
            common_elements.append(value)

    print("\nCommon Elements:", common_elements)
    print("Number of Common Elements:", len(common_elements))

subsetvalidator()