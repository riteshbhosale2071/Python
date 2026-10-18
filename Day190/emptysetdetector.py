def emptysetdetector():
    print("Empty Set Detector :")

    n = int(input("Enter the number of elements in the set: "))

    if n < 0:
        print("Number of elements cannot be negative.")
        return

    elements = []

    for i in range(n):
        value = input("Enter element " + str(i + 1) + ": ")

        if value not in elements:
            elements.append(value)

    print("\nSet Analysis :")
    print("Set:", elements)
    print("Number of Elements Entered:", n)
    print("Number of Distinct Elements:", len(elements))

    if len(elements) == 0:
        print("Result: The set is empty.")
        print("Mathematical Representation: A = {}")
    else:
        print("Result: The set is not empty.")
        print("Mathematical Representation: A =", elements)

    print("\nAdditional Analysis :")

    if len(elements) == 0:
        print("The set contains no elements.")
        print("The set is a subset of every set.")
    elif len(elements) == 1:
        print("The set contains exactly one distinct element.")
    else:
        print("The set contains multiple distinct elements.")

    duplicate_count = n - len(elements)
    print("Duplicate Entries:", duplicate_count)

emptysetdetector()