def universalsetcomplement():
    print("Universal Set Complement Calculator :")

    n = int(input("Enter the number of elements in the universal set: "))

    if n < 0:
        print("Number of elements cannot be negative.")
        return

    universal_set = []

    for i in range(n):
        value = input("Enter universal set element " + str(i + 1) + ": ")

        if value not in universal_set:
            universal_set.append(value)

    m = int(input("\nEnter the number of elements in Set A: "))

    if m < 0:
        print("Number of elements cannot be negative.")
        return

    set_a = []

    for i in range(m):
        value = input("Enter element " + str(i + 1) + " of Set A: ")

        if value not in set_a:
            set_a.append(value)

    invalid_elements = []

    for value in set_a:
        if value not in universal_set:
            invalid_elements.append(value)

    if invalid_elements:
        print("\nError: Set A contains elements outside the universal set.")
        print("Invalid Elements:", invalid_elements)
        return

    complement = []

    for value in universal_set:
        if value not in set_a:
            complement.append(value)

    print("\nComplement Results :")
    print("Universal Set U:", universal_set)
    print("Set A:", set_a)
    print("Complement of A (A'):", complement)
    print("Cardinality of U:", len(universal_set))
    print("Cardinality of A:", len(set_a))
    print("Cardinality of A':", len(complement))

    print("\nComplement Verification :")

    union = set_a.copy()

    for value in complement:
        if value not in union:
            union.append(value)

    intersection = []

    for value in set_a:
        if value in complement:
            intersection.append(value)

    print("A Union A':", union)
    print("A Intersection A':", intersection)

    if len(union) == len(universal_set) and all(
        value in union for value in universal_set
    ):
        print("Verified: A Union A' equals the universal set.")

    if len(intersection) == 0:
        print("Verified: A Intersection A' is the empty set.")

    print("\nComplement calculation completed successfully.")

universalsetcomplement()