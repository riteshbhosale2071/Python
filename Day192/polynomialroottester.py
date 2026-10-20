def polynomialroottester():
    print("Polynomial Root Tester :")

    try:
        n = int(input("Enter the number of terms in the polynomial: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of terms must be greater than zero.")
        return

    polynomial = {}

    for i in range(n):
        print("\nTerm", i + 1)

        try:
            coefficient = float(input("Enter coefficient: "))
            exponent = int(input("Enter exponent of x: "))
        except ValueError:
            print("Invalid input! Enter valid numbers.")
            return

        if exponent < 0:
            print("Exponent must be a non-negative integer.")
            return

        if exponent in polynomial:
            polynomial[exponent] += coefficient
        else:
            polynomial[exponent] = coefficient

    try:
        test_value = float(input("\nEnter the value to test as a root: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    result = 0

    for exponent, coefficient in polynomial.items():
        result += coefficient * (test_value ** exponent)

    print("\nPolynomial Root Test Results :")
    print("Polynomial Coefficients:", polynomial)
    print("Test Value:", test_value)
    print("Polynomial Value:", round(result, 8))

    if abs(result) < 1e-8:
        print("Result: The given value is a root of the polynomial.")
    else:
        print("Result: The given value is not a root of the polynomial.")

    print("\nVerification :")

    for exponent in sorted(polynomial.keys(), reverse=True):
        coefficient = polynomial[exponent]
        term_value = coefficient * (test_value ** exponent)

        print(
            "Term:", coefficient, "x^", exponent,
            "| Value:", round(term_value, 8)
        )

    print("\nFinal Polynomial Value:", round(result, 8))

polynomialroottester()