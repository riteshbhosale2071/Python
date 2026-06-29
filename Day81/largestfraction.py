def largestfraction():
    n = int(input("Enter number of fractions: "))

    largest_numerator = 0
    largest_denominator = 1

    for i in range(n):
        numerator = int(input(f"Enter numerator of fraction {i+1}: "))
        denominator = int(input(f"Enter denominator of fraction {i+1}: "))

        if numerator * largest_denominator > largest_numerator * denominator:
            largest_numerator = numerator
            largest_denominator = denominator

    print("Largest Fraction =", largest_numerator, "/", largest_denominator)

largestfraction()