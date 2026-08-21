def differenceofsquares():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a ** 2 - b ** 2
    factor1 = a - b
    factor2 = a + b

    print("Difference of Squares:", result)
    print("Using (a - b)(a + b):", factor1 * factor2)

differenceofsquares()