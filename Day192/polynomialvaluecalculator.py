def polynomialvaluecalculator():
    print("Polynomial Value Calculator :")

    try:
        n = int(input("Enter the number of terms in the polynomial: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of terms must be greater than zero.")
        return

    terms = {}

    for i in range(n):
        print("\nTerm", i + 1)

        try:
            coefficient = float(input("Enter the coefficient: "))
            exponent = int(input("Enter the exponent of x: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            return

        if exponent < 0:
            print("Exponent must be a non-negative integer.")
            return

        if exponent in terms:
            terms[exponent] += coefficient
        else:
            terms[exponent] = coefficient

    try:
        x = float(input("\nEnter the value of x: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    polynomial_value = 0

    for exponent, coefficient in terms.items():
        polynomial_value += coefficient * (x ** exponent)

    print("\nPolynomial Calculation :")
    print("Value of x:", x)
    print("Polynomial Terms:")

    for exponent in sorted(terms.keys(), reverse=True):
        coefficient = terms[exponent]
        print("Coefficient:", coefficient, "| Exponent:", exponent)

    print("\nResult :")
    print("Polynomial Value:", round(polynomial_value, 6))

    if polynomial_value > 0:
        print("Result: The polynomial value is positive.")
    elif polynomial_value < 0:
        print("Result: The polynomial value is negative.")
    else:
        print("Result: The polynomial value is zero.")

polynomialvaluecalculator()