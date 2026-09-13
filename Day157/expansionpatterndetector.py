def expansionpatterndetector():
    print("Expansion Pattern Detector :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    n = int(input("Enter power n: "))

    if n < 0:
        print("Power must be a non-negative integer.")
        return

    coefficient = 1
    terms = []

    for r in range(n + 1):
        if r > 0:
            coefficient = coefficient * (n - r + 1) // r

        terms.append(coefficient)

    print("\nExpansion Pattern :")
    print("Binomial coefficients:")

    for coefficient in terms:
        print(coefficient, end=" ")

    print("\n\nPower of a:")
    for r in range(n + 1):
        print(n - r, end=" ")

    print("\n\nPower of b:")
    for r in range(n + 1):
        print(r, end=" ")

    print("\n\nPattern:")
    print("The power of a decreases by 1.")
    print("The power of b increases by 1.")
    print("The binomial coefficients follow Pascal's Triangle.")

    if a == b:
        print("Since a and b are equal, the terms have equal base values.")
    else:
        print("The expansion contains different powers of a and b.")

expansionpatterndetector()