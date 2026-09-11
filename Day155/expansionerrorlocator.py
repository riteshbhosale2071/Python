def expansionerrorlocator():
    print("Expansion Error Locator :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    n = int(input("Enter power n: "))

    if n < 0:
        print("Power must be a non-negative integer.")
        return

    expected = []
    coefficient = 1

    for r in range(n + 1):
        if r > 0:
            coefficient = coefficient * (n - r + 1) // r

        term = coefficient * (a ** (n - r)) * (b ** r)
        expected.append(term)

    print("\nExpected terms:")
    for i in range(len(expected)):
        print("Term", i + 1, ":", expected[i])

    print("\nEnter the terms of your expansion:")
    entered = []

    for i in range(n + 1):
        value = int(input("Term " + str(i + 1) + ": "))
        entered.append(value)

    print("\nError Report :")

    errors = 0

    for i in range(n + 1):
        if entered[i] != expected[i]:
            print("Error in Term", i + 1)
            print("Expected:", expected[i])
            print("Entered:", entered[i])
            errors = errors + 1

    if errors == 0:
        print("No errors found. Expansion is correct.")
    else:
        print("Total errors found:", errors)

expansionerrorlocator()