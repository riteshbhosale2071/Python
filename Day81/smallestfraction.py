def smallestfraction():
    n = int(input("Enter number of fractions: "))

    numerator = int(input("Enter numerator of fraction 1: "))
    denominator = int(input("Enter denominator of fraction 1: "))

    smallest_numerator = numerator
    smallest_denominator = denominator

    for i in range(2, n + 1):
        numerator = int(input(f"Enter numerator of fraction {i}: "))
        denominator = int(input(f"Enter denominator of fraction {i}: "))

        if numerator * smallest_denominator < smallest_numerator * denominator:
            smallest_numerator = numerator
            smallest_denominator = denominator

    print("Smallest Fraction =", smallest_numerator, "/", smallest_denominator)

smallestfraction()