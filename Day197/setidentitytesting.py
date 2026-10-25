def setidentitytesting():
    print("Set Identity Testing :")

    def read_set(set_name):
        try:
            count = int(input("Enter the number of elements in " + set_name + ": "))
        except ValueError:
            print("Invalid input! Enter an integer.")
            return None

        if count < 0:
            print("The number of elements cannot be negative.")
            return None

        elements = set()

        for i in range(count):
            value = input("Enter element " + str(i + 1) + ": ").strip()

            if value == "":
                print("Elements cannot be empty.")
                return None

            elements.add(value)

        return elements

    set_a = read_set("Set A")

    if set_a is None:
        return

    set_b = read_set("Set B")

    if set_b is None:
        return

    print("\nSet A:", set_a)
    print("Set B:", set_b)

    print("\nSet Identity Verification :")

    union_ab = set_a | set_b
    union_ba = set_b | set_a

    intersection_ab = set_a & set_b
    intersection_ba = set_b & set_a

    difference_ab = set_a - set_b
    difference_ba = set_b - set_a

    symmetric_ab = set_a ^ set_b
    symmetric_ba = set_b ^ set_a

    print("\n1. Commutative Law of Union")
    print("A union B:", union_ab)
    print("B union A:", union_ba)
    print("Identity holds:", union_ab == union_ba)

    print("\n2. Commutative Law of Intersection")
    print("A intersection B:", intersection_ab)
    print("B intersection A:", intersection_ba)
    print("Identity holds:", intersection_ab == intersection_ba)

    print("\n3. Difference Identity")
    print("A - B:", difference_ab)
    print("B - A:", difference_ba)
    print("Differences are equal:", difference_ab == difference_ba)

    print("\n4. Symmetric Difference Identity")
    print("A symmetric difference B:", symmetric_ab)
    print("B symmetric difference A:", symmetric_ba)
    print("Identity holds:", symmetric_ab == symmetric_ba)

    print("\n5. Idempotent Law")
    print("A union A equals A:", (set_a | set_a) == set_a)
    print("A intersection A equals A:", (set_a & set_a) == set_a)

    print("\n6. Identity Laws")
    empty_set = set()

    print("A union empty set equals A:", (set_a | empty_set) == set_a)
    print("A intersection empty set equals empty set:",
          (set_a & empty_set) == empty_set)

    print("\n7. Distributive Law")
    left_union = set_a & (set_b | empty_set)
    right_union = (set_a & set_b) | (set_a & empty_set)

    print("A intersection (B union empty set):", left_union)
    print("(A intersection B) union (A intersection empty set):",
          right_union)
    print("Identity holds:", left_union == right_union)

    print("\nFinal Result :")

    if union_ab == union_ba and intersection_ab == intersection_ba:
        print("Set union and intersection commutative identities are verified.")
    else:
        print("Some set identities failed verification.")

    print("Set identity testing completed successfully.")

setidentitytesting()