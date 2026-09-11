def expansioncoefficientextractor():
    print("Expansion Coefficient Extractor :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    n = int(input("Enter power n: "))
    r = int(input("Enter term position (1 to n+1): "))

    if n < 0 or r < 1 or r > n + 1:
        print("Invalid input.")
        return

    k = r - 1
    coefficient = 1

    for i in range(1, k + 1):
        coefficient = coefficient * (n - i + 1) // i

    value = coefficient * (a ** (n - k)) * (b ** k)

    print("\nExpansion Result :")
    print("Term number:", r)
    print("Binomial coefficient:", coefficient)
    print("Term value:", value)

expansioncoefficientextractor()