def setequalitychecker():
    print("Set Equality Checker :")

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

    print("\nSet Comparison Results :")
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Number of Elements in Set A:", len(set_a))
    print("Number of Elements in Set B:", len(set_b))

    if len(set_a) == len(set_b):
        print("Both sets have the same number of distinct elements.")
    else:
        print("Both sets have different numbers of distinct elements.")

    if len(set_a) == len(set_b):
        equal = True

        for value in set_a:
            if value not in set_b:
                equal = False
                break

        if equal:
            print("Result: Set A and Set B are equal.")
            print("Both sets contain exactly the same elements.")
        else:
            print("Result: Set A and Set B are not equal.")
    else:
        print("Result: Set A and Set B are not equal.")

    only_a = []
    only_b = []

    for value in set_a:
        if value not in set_b:
            only_a.append(value)

    for value in set_b:
        if value not in set_a:
            only_b.append(value)

    common_elements = []

    for value in set_a:
        if value in set_b:
            common_elements.append(value)

    print("\nElement Analysis :")
    print("Common Elements:", common_elements)
    print("Elements Only in Set A:", only_a)
    print("Elements Only in Set B:", only_b)

    if len(only_a) == 0 and len(only_b) == 0:
        print("Both sets have identical membership.")
    else:
        print("The sets differ in their elements.")

setequalitychecker()