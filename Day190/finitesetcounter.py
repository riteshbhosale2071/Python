def finitesetcounter():
    print("Finite Set Counter :")

    n = int(input("Enter the number of elements to enter: "))

    if n < 0:
        print("Number of elements cannot be negative.")
        return

    elements = []

    for i in range(n):
        value = input("Enter element " + str(i + 1) + ": ")

        if value not in elements:
            elements.append(value)

    print("\nFinite Set Analysis :")
    print("Set:", elements)
    print("Number of Entries:", n)
    print("Number of Distinct Elements:", len(elements))

    if len(elements) == 0:
        print("The set is empty.")
        print("Cardinality: 0")
    else:
        print("The set is finite.")
        print("Cardinality:", len(elements))

    print("\nCardinality Classification :")

    if len(elements) == 0:
        print("Classification: Empty finite set.")
    elif len(elements) == 1:
        print("Classification: Singleton set.")
    else:
        print("Classification: Finite set with multiple elements.")

    print("\nElement Listing :")

    for index, value in enumerate(elements, start=1):
        print("Element", index, ":", value)

    print("\nTotal Distinct Elements:", len(elements))
    print("Duplicate Entries:", n - len(elements))

finitesetcounter()