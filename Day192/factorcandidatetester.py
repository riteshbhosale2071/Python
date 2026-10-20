def factorcandidatetester():
    print("Factor Candidate Tester :")

    try:
        n = int(input("Enter the number of polynomial terms: "))
    except ValueError:
        print("Invalid input! Enter an integer.")
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
        candidate = float(input("\nEnter the factor candidate (r): "))
    except ValueError:
        print("Invalid input! Enter a valid number.")
        return

    result = 0

    for exponent, coefficient in polynomial.items():
        result += coefficient * (candidate ** exponent)

    print("\nFactor Candidate Test :")
    print("Polynomial:", polynomial)
    print("Candidate:", candidate)
    print("Polynomial Value at r:", round(result, 8))

    if abs(result) < 1e-8:
        print("Result: x -", candidate, "is a factor of the polynomial.")
        print("The candidate is a root of the polynomial.")
    else:
        print("Result: x -", candidate, "is not a factor of the polynomial.")
        print("The candidate is not a root of the polynomial.")

    print("\nTerm-by-Term Evaluation :")

    for exponent in sorted(polynomial.keys(), reverse=True):
        coefficient = polynomial[exponent]
        term_value = coefficient * (candidate ** exponent)

        print(
            "Coefficient:", coefficient,
            "| Exponent:", exponent,
            "| Term Value:", round(term_value, 8)
        )

    print("\nFinal Evaluation:", round(result, 8))

factorcandidatetester()