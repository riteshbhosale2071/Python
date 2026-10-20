def polynomialsubtraction():
    print("Polynomial Subtraction :")

    def input_polynomial(name):
        try:
            n = int(input("Enter the number of terms in " + name + ": "))
        except ValueError:
            print("Invalid input! Enter an integer.")
            return None

        if n < 0:
            print("Number of terms cannot be negative.")
            return None

        polynomial = {}

        for i in range(n):
            print("\n" + name + " - Term", i + 1)

            try:
                coefficient = float(input("Enter coefficient: "))
                exponent = int(input("Enter exponent of x: "))
            except ValueError:
                print("Invalid input! Enter valid numbers.")
                return None

            if exponent < 0:
                print("Exponent must be a non-negative integer.")
                return None

            if exponent in polynomial:
                polynomial[exponent] += coefficient
            else:
                polynomial[exponent] = coefficient

        return polynomial

    def display_polynomial(polynomial):
        terms = []

        for exponent in sorted(polynomial.keys(), reverse=True):
            coefficient = polynomial[exponent]

            if coefficient == 0:
                continue

            absolute_coefficient = abs(coefficient)

            if exponent == 0:
                term = str(absolute_coefficient)
            elif exponent == 1:
                term = "x" if absolute_coefficient == 1 else str(absolute_coefficient) + "x"
            else:
                term = "x^" + str(exponent) if absolute_coefficient == 1 else str(absolute_coefficient) + "x^" + str(exponent)

            if not terms:
                terms.append("-" + term if coefficient < 0 else term)
            else:
                terms.append((" - " if coefficient < 0 else " + ") + term)

        return "".join(terms) if terms else "0"

    polynomial_a = input_polynomial("Polynomial A")

    if polynomial_a is None:
        return

    polynomial_b = input_polynomial("Polynomial B")

    if polynomial_b is None:
        return

    result = polynomial_a.copy()

    for exponent, coefficient in polynomial_b.items():
        if exponent in result:
            result[exponent] -= coefficient
        else:
            result[exponent] = -coefficient

    print("\nPolynomial Subtraction Results :")
    print("Polynomial A:", display_polynomial(polynomial_a))
    print("Polynomial B:", display_polynomial(polynomial_b))
    print("Difference (A - B):", display_polynomial(result))

    print("\nCoefficient Subtraction :")

    for exponent in sorted(result.keys(), reverse=True):
        coefficient_a = polynomial_a.get(exponent, 0)
        coefficient_b = polynomial_b.get(exponent, 0)
        coefficient_difference = result[exponent]

        print(
            "Exponent:", exponent,
            "| A:", coefficient_a,
            "| B:", coefficient_b,
            "| Difference:", coefficient_difference
        )

    nonzero_exponents = [
        exponent for exponent, coefficient in result.items()
        if coefficient != 0
    ]

    if nonzero_exponents:
        print("\nDegree of Resulting Polynomial:", max(nonzero_exponents))
    else:
        print("\nResult is the zero polynomial.")

polynomialsubtraction()